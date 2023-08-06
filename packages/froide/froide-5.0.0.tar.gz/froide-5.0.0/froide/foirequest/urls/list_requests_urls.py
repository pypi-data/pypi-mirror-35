from django.utils.six import text_type as str
from django.urls import reverse
from django.conf.urls import url, include
from django.utils.translation import pgettext
from django.shortcuts import redirect

from ..views import (
    list_requests, list_unchecked, delete_draft,
)
from ..filters import FOIREQUEST_FILTERS


STATUS_URLS = [str(x[0]) for x in FOIREQUEST_FILTERS]

urlpatterns = [
    url(r'^%s/$' % pgettext('URL part', 'not-foi'), list_requests,
        kwargs={'not_foi': True}, name='foirequest-list_not_foi'),

    # Old feed URL
    url(r'^%s/feed/$' % pgettext('URL part', 'latest'),
        lambda r: redirect(reverse('foirequest-list_feed_atom'), permanent=True),
        name='foirequest-feed_latest_atom'),
    url(r'^%s/rss/$' % pgettext('URL part', 'latest'),
        lambda r: redirect(reverse('foirequest-list_feed'), permanent=True),
        name='foirequest-feed_latest'),

    url(r'^unchecked/$', list_unchecked, name='foirequest-list_unchecked'),
    url(r'^delete-draft$', delete_draft, name='foirequest-delete_draft'),
]

foirequest_urls = [
    url(r'^$', list_requests, name='foirequest-list'),
    url(r'^feed/$', list_requests,
        kwargs={'feed': 'atom'}, name='foirequest-list_feed_atom'),
    url(r'^rss/$', list_requests,
        kwargs={'feed': 'rss'}, name='foirequest-list_feed'),

    # Translators: part in request filter URL
    url(r'^%s/(?P<topic>[-\w]+)/$' % pgettext('URL part', 'topic'),
        list_requests, {}, 'foirequest-list'),
    url(r'^%s/(?P<topic>[-\w]+)/feed/$' % pgettext('URL part', 'topic'),
        list_requests, kwargs={'feed': 'atom'}, name='foirequest-list_feed_atom'),
    url(r'^%s/(?P<topic>[-\w]+)/rss/$' % pgettext('URL part', 'topic'),
        list_requests, kwargs={'feed': 'rss'}, name='foirequest-list_feed'),

    # Translators: part in request filter URL
    url(r'^%s/(?P<tag>[-\w]+)/$' % pgettext('URL part', 'tag'), list_requests,
        name='foirequest-list'),
    url(r'^%s/(?P<tag>[-\w]+)/feed/$' % pgettext('URL part', 'tag'),
        list_requests, kwargs={'feed': 'atom'}, name='foirequest-list_feed_atom'),
    url(r'^%s/(?P<tag>[-\w]+)/rss/$' % pgettext('URL part', 'tag'),
        list_requests, kwargs={'feed': 'rss'}, name='foirequest-list_feed'),

    # Translators: part in request filter URL
    url(r'^%s/(?P<publicbody>[-\w]+)/$' % pgettext('URL part', 'to'),
        list_requests, name='foirequest-list'),
    url(r'^%s/(?P<publicbody>[-\w]+)/feed/$' % pgettext('URL part', 'to'),
        list_requests, kwargs={'feed': 'atom'}, name='foirequest-list_feed_atom'),
    url(r'^%s/(?P<publicbody>[-\w]+)/rss/$' % pgettext('URL part', 'to'),
        list_requests, kwargs={'feed': 'rss'}, name='foirequest-list_feed'),

] + [url(r'^(?P<status>%s)/$' % status, list_requests, name='foirequest-list')
        for status in STATUS_URLS
] + [url(r'^(?P<status>%s)/feed/$' % status, list_requests,
        kwargs={'feed': 'atom'}, name='foirequest-list_feed_atom')
        for status in STATUS_URLS
] + [url(r'^(?P<status>%s)/rss/$' % status, list_requests,
        kwargs={'feed': 'rss'}, name='foirequest-list_feed')
        for status in STATUS_URLS]

urlpatterns += foirequest_urls

urlpatterns += [
    url(r'^(?P<jurisdiction>[-\w]+)/', include(foirequest_urls))
]
