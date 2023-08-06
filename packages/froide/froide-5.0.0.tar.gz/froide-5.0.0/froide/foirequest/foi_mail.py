import base64
import json
import zipfile
from email.utils import parseaddr
import random

from django.conf import settings
from django.core.mail import get_connection, EmailMessage, mail_managers
from django.urls import reverse
from django.utils.translation import override, ugettext_lazy as _
from django.utils.six import BytesIO, string_types

from froide.helper.email_utils import (EmailParser, get_unread_mails,
                                       make_address)
from froide.helper.name_generator import get_name_from_number

from .utils import get_publicbody_for_email
from .pdf_generator import FoiRequestPDFGenerator

unknown_foimail_message = _('''We received an FoI mail to this address: %(address)s.
No corresponding request could be identified, please investigate! %(url)s
''')

spam_message = _('''We received a possible spam mail to this address: %(address)s.
Please investigate! %(url)s
''')


def send_foi_mail(subject, message, from_email, recipient_list,
                  attachments=None, fail_silently=False, **kwargs):
    backend = None
    if kwargs.get('dsn'):
        if hasattr(settings, 'FOI_EMAIL_BACKEND'):
            backend = settings.FOI_EMAIL_BACKEND

    if not backend:
        backend = settings.EMAIL_BACKEND
    connection = get_connection(
        backend=backend,
        username=settings.FOI_EMAIL_HOST_USER,
        password=settings.FOI_EMAIL_HOST_PASSWORD,
        host=settings.FOI_EMAIL_HOST,
        port=settings.FOI_EMAIL_PORT,
        use_tls=settings.FOI_EMAIL_USE_TLS,
        fail_silently=fail_silently
    )
    headers = {}
    if settings.FOI_EMAIL_FIXED_FROM_ADDRESS:
        name, mailaddr = parseaddr(from_email)
        from_address = settings.FOI_EMAIL_HOST_FROM
        from_email = make_address(from_address, name)
        headers['Reply-To'] = make_address(mailaddr, name)
    else:
        headers['Reply-To'] = from_email

    if kwargs.get('read_receipt'):
        headers['Disposition-Notification-To'] = from_email
    if kwargs.get('delivery_receipt'):
        headers['Return-Receipt-To'] = from_email
    if kwargs.get('froide_message_id'):
        headers['X-Froide-Message-Id'] = kwargs.get('froide_message_id')

    email = EmailMessage(subject, message, from_email, recipient_list,
                         connection=connection, headers=headers)
    if attachments is not None:
        for name, data, mime_type in attachments:
            email.attach(name, data, mime_type)
    return email.send()


def _process_mail(mail_bytes, mail_type=None, manual=False):
    parser = EmailParser()
    if mail_type is None:
        email = parser.parse(BytesIO(mail_bytes))
    elif mail_type == 'postmark':
        email = parser.parse_postmark(json.loads(mail_bytes.decode('utf-8')))
    return _deliver_mail(email, mail_bytes=mail_bytes, manual=manual)


def create_deferred(secret_mail, mail_bytes, spam=False,
                    subject=_('Unknown FoI-Mail Recipient'),
                    body=unknown_foimail_message, request=None):
    from .models import DeferredMessage

    mail_string = ''
    if mail_bytes is not None:
        mail_string = base64.b64encode(mail_bytes).decode("utf-8")
    DeferredMessage.objects.create(
        recipient=secret_mail,
        mail=mail_string,
        spam=spam,
        request=request
    )
    with override(settings.LANGUAGE_CODE):
        url = reverse('admin:foirequest_deferredmessage_changelist')
        mail_managers(
            subject,
            body % {
                'address': secret_mail,
                'url': settings.SITE_URL + url
            }
        )


def get_alternative_mail(req):
    name = get_name_from_number(req.pk)
    domains = settings.FOI_EMAIL_DOMAIN
    if isinstance(domains, string_types):
        domains = [domains]
    if len(domains) > 1:
        domains = domains[1:]

    random.shuffle(domains)
    return '%s_%s@%s' % (name, req.pk, domains[0])


def get_foirequest_from_mail(email):
    from .models import FoiRequest

    if '_' in email:
        name, domain = email.split('@', 1)
        hero, num = name.rsplit('_', 1)
        try:
            num = int(num)
        except ValueError:
            return None
        hero_name = get_name_from_number(num)
        if hero_name != hero:
            return None
        try:
            return FoiRequest.objects.get(pk=num)
        except FoiRequest.DoesNotExist:
            return None

    else:
        try:
            return FoiRequest.objects.get_by_secret_mail(email)
        except FoiRequest.DoesNotExist:
            return None


def _deliver_mail(email, mail_bytes=None, manual=False):
    received_list = (email['to'] + email['cc'] +
                     email['resent_to'] + email['resent_cc'])
    received_list = [(r[0], r[1].lower()) for r in received_list]

    domains = settings.FOI_EMAIL_DOMAIN
    if isinstance(domains, string_types):
        domains = [domains]

    def mail_filter(x):
        return x[1].endswith(tuple(["@%s" % d for d in domains]))

    received_list = [r for r in received_list if mail_filter(r)]

    # normalize to first FOI_EMAIL_DOMAIN
    received_list = [(x[0], '@'.join(
        (x[1].split('@')[0], domains[0]))) for x in received_list]

    sender_email = email['from'][1]

    already = set()
    for received in received_list:
        recipient_email = received[1]
        if recipient_email in already:
            continue
        already.add(recipient_email)
        foirequest, pb = check_delivery_conditions(
            recipient_email, sender_email, mail_bytes, manual=manual
        )
        if foirequest is not None:
            add_message_from_email(foirequest, email, publicbody=pb)


def add_message_from_email(foirequest, email, publicbody=None):
    from .services import ReceiveEmailService

    service = ReceiveEmailService(
        email,
        foirequest=foirequest,
        publicbody=publicbody
    )
    service.process()


def check_delivery_conditions(recipient_mail, sender_email,
                              mail_bytes, manual=False):
    from .models import DeferredMessage

    foirequest = get_foirequest_from_mail(recipient_mail)
    if not foirequest:
        deferred = DeferredMessage.objects.filter(
            recipient=recipient_mail, request__isnull=False
        )
        if len(deferred) == 0 or len(deferred) > 1:
            # Can't do automatic matching!
            create_deferred(
                recipient_mail, mail_bytes,
                spam=False
            )
            return None, None
        else:
            deferred = deferred[0]
            foirequest = deferred.request

    pb = None
    if not manual:
        if foirequest.closed:
            # Request is closed and will not receive messages
            return None, None

        # Check for spam
        pb = get_publicbody_for_email(sender_email, foirequest)

        if pb is None:
            create_deferred(
                recipient_mail, mail_bytes,
                spam=True,
                subject=_('Possible Spam Mail received'),
                body=spam_message,
                request=foirequest
            )
            return None, None
    return foirequest, pb


def _fetch_mail():
    for rfc_data in get_unread_mails(
            settings.FOI_EMAIL_HOST_IMAP,
            settings.FOI_EMAIL_PORT_IMAP,
            settings.FOI_EMAIL_ACCOUNT_NAME,
            settings.FOI_EMAIL_ACCOUNT_PASSWORD,
            ssl=settings.FOI_EMAIL_USE_SSL):
        yield rfc_data


def fetch_and_process():
    count = 0
    for rfc_data in _fetch_mail():
        _process_mail(rfc_data)
        count += 1
    return count


def package_foirequest(foirequest):
    zfile_obj = BytesIO()
    with override(settings.LANGUAGE_CODE):
        zfile = zipfile.ZipFile(zfile_obj, 'w')
        last_date = None
        date_count = 1
        path = str(foirequest.pk)
        pdf_generator = FoiRequestPDFGenerator(foirequest)
        correspondence_bytes = pdf_generator.get_pdf_bytes()
        zfile.writestr('%s/%s.pdf' % (path, foirequest.pk), correspondence_bytes)
        for message in foirequest.messages:
            current_date = message.timestamp.date()
            date_prefix = current_date.isoformat()
            if current_date == last_date:
                date_count += 1
            else:
                date_count = 1
            date_prefix += '_%d' % date_count
            last_date = current_date

            att_queryset = message.foiattachment_set.filter(
                is_redacted=False,
                is_converted=False
            )

            for attachment in att_queryset:
                if not attachment.file:
                    continue
                filename = '%s/%s-%s' % (path, date_prefix, attachment.name)
                zfile.write(attachment.file.path, arcname=filename)
        zfile.close()
    return zfile_obj.getvalue()
