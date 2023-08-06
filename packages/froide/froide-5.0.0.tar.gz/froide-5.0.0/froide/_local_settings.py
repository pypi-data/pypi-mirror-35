# -*- coding: utf-8 -*-
import os

from .settings import Base, German, SSLNginxProduction


class Dev(German, Base):

    gettext = lambda s: s
    LANGUAGES = (
        ('de', gettext('German')),
        # ('en', gettext('English')),
    )

    # LANGUAGES = (
    #     ('en', gettext('English')),
    #     ('de', gettext('German')),
    #     ('fi', gettext('Finnish')),
    #     ('sv', gettext('Swedish')),
    # )

    TASTYPIE_FULL_DEBUG = True

    @property
    def INSTALLED_APPS(self):
        installed = super(Dev, self).INSTALLED_APPS
        installed.default += ['debug_toolbar']
        installed.default += ['foiidea']
        return installed

    DEBUG = True

    @property
    def GEOIP_PATH(self):
        return os.path.join(super(Dev, self).PROJECT_ROOT, '..', 'data')

    ADMINS = (
        ('Stefan Wehrmeyer', 'mail@stefanwehrmeyer.com'),
    )
    MANAGERS = (
        ('Team', 'team@fragdenstaat.de'),
    )

    INTERNAL_IPS = ('127.0.0.1',)

    USE_X_ACCEL_REDIRECT = False
    X_ACCEL_REDIRECT_PREFIX = '/protected'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'fragdenstaat_2',                      # Or path to database file if using sqlite3.
            'USER': 'fragdenstaat',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            'OPTIONS': {
                'autocommit': True
            }
        }
    }

    SOUTH_MIGRATION_MODULES = {}

    MIDDLEWARE_CLASSES = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        # 'djangosecure.middleware.SecurityMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.common.CommonMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',

    ]

    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            'LOCATION': 'unique-snowflake'
        }
    }

    # ######### Debug ###########

    CELERY_ALWAYS_EAGER = True

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
            'URL': 'http://127.0.0.1:8983/solr/fragdenstaat'
        }
    }

    # HAYSTACK_CONNECTIONS = {
    #     'default': {
    #         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    #     }
    # }

    SITE_NAME = "Frag den Staat"
    SITE_EMAIL = "info@fragdenstaat.de"
    SITE_URL = 'http://localhost:8000'

    SECRET_URLS = {
        "admin": "admin",
    }

    @property
    def FROIDE_CONFIG(self):
        config = super(Dev, self).FROIDE_CONFIG
        config.update(dict(
            user_can_hide_web=True,
            public_body_officials_public=False,
            public_body_officials_email_public=False,
            default_law=2,
            doc_conversion_binary='/Applications/LibreOffice.app/Contents/MacOS/soffice',
            dryrun=False,
            dryrun_domain="fragdenstaat.stefanwehrmeyer.com",
            allow_pseudonym=True,
            can_make_meta_request=True
        ))
        return config

    DEFAULT_FROM_EMAIL = 'info@fragdenstaat.de'
    EMAIL_SUBJECT_PREFIX = '[AdminFragDenStaat] '

    # dev use:
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
    # CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    CELERY_EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class FragDenStaat(German, SSLNginxProduction):
    ADMINS = (('FragDenStaat.de', 'mail@fragdenstaat.de'),)
    MANAGERS = (('FragDenStaat.de', 'mail@fragdenstaat.de'),)

    ALLOWED_HOSTS = ('fragdenstaat.de',)
    CACHES = {
        'default': {
            'LOCATION': 'unique-snowflake',
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
        }
    }
    CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fragdenstaat',
            'TIME_ZONE': 'UTC',
            'OPTIONS': {},
            'HOST': '',
            'USER': 'fragdenstaat',
            'PASSWORD': 'nxw8fyhfbliasef',
            'PORT': ''
        }
    }
    SOUTH_MIGRATION_MODULES = {}

    DEFAULT_FROM_EMAIL = 'info@fragdenstaat.de'
    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
    EMAIL_HOST_PASSWORD = 'aBtwyC/9wKybE'
    EMAIL_HOST_USER = 'mail@fragdenstaat.de'
    EMAIL_SUBJECT_PREFIX = '[AdminFragDenStaat] '
    EMAIL_USE_TLS = True
    EMAIL_PORT = 25
    FOI_EMAIL_ACCOUNT_NAME = 'foimail@fragdenstaat.de'
    FOI_EMAIL_ACCOUNT_PASSWORD = 'TmFIGzMO3dIkk'
    FOI_EMAIL_DOMAIN = 'fragdenstaat.de'
    FOI_EMAIL_FIXED_FROM_ADDRESS = False
    FOI_EMAIL_FUNC = None
    FOI_EMAIL_HOST = 'localhost'
    FOI_EMAIL_HOST_FROM = 'foimail@fragdenstaat.de'
    FOI_EMAIL_HOST_IMAP = 'localhost'
    FOI_EMAIL_HOST_PASSWORD = 'TmFIGzMO3dIkk'
    FOI_EMAIL_HOST_USER = 'foimail@fragdenstaat.de'
    FOI_EMAIL_PORT = 25
    FOI_EMAIL_PORT_IMAP = 143
    FOI_EMAIL_USE_SSL = False
    FOI_EMAIL_USE_TLS = True
    FOI_MEDIA_PATH = 'foi'

    @property
    def FROIDE_CONFIG(self):
        config = super(FragDenStaat, self).FROIDE_CONFIG
        config.update(dict(
            user_can_hide_web=True,
            public_body_officials_public=True,
            public_body_officials_email_public=False,
            default_law=2,
            doc_conversion_binary="/usr/lib/libreoffice/program/soffice",
            dryrun=False,
            dryrun_domain="fragdenstaat.stefanwehrmeyer.com",
            allow_pseudonym=True,
            api_activated=True,
            search_engine_query='http://www.google.de/search?as_q=%(query)s&as_epq=&as_oq=&as_eq=&hl=en&lr=&cr=&as_ft=i&as_filetype=&as_qdr=all&as_occt=any&as_dt=i&as_sitesearch=%(domain)s&as_rights=&safe=images',
        ))
        return config

    GEOIP_PATH = '/var/www/fragdenstaat.de/data'

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
            'URL': 'http://127.0.0.1:8080/solr/fragdenstaat.de'
        }
    }
    HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

    LOGGING = {
        'loggers': {
            'froide': {
                'level': 'INFO',
                'propagate': True,
                'handlers': ['normal']
            },
            'sentry.errors': {
                'handlers': ['normal'],
                'propagate': False,
                'level': 'DEBUG'
            },
            'django.request': {
                'level': 'ERROR',
                'propagate': True,
                'handlers': ['mail_admins', 'normal']
            },
            'raven': {
                'handlers': ['normal'],
                'propagate': False,
                'level': 'DEBUG'
            }
        },
        'disable_existing_loggers': False,
        'handlers': {
            'normal': {
                'filename': '/var/www/fragdenstaat.de/logs/froide.log',
                'class': 'logging.FileHandler',
                'level': 'INFO'
            },
            'sentry': {
                'class': 'raven.contrib.django.handlers.SentryHandler',
                'level': 'ERROR'
            },
            'mail_admins': {
                'class': 'django.utils.log.AdminEmailHandler',
                'filters': ['require_debug_false'],
                'level': 'ERROR'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            }
        },
        'version': 1,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'root': {
            'handlers': ['sentry'],
            'level': 'WARNING'
        }
    }
    MANAGERS = (('FragDenStaat.de', 'mail@fragdenstaat.de'),)
    MEDIA_ROOT = '/var/www/fragdenstaat.de/storage/files'
    MEDIA_URL = '/files/'

    MIDDLEWARE_CLASSES = [
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.common.CommonMiddleware',
    ]

    SECRET_KEY = 'FMHIAUEHRPCMPRIAEifugaisuflfkaldgGLIWR37rtW(dH:FGA'
    SECRET_URLS = {'admin': 'fds-admin'}

    SERVER_EMAIL = 'info@fragdenstaat.de'

    SITE_EMAIL = 'info@fragdenstaat.de'
    SITE_ID = 1
    SITE_NAME = 'Frag den Staat'
    SITE_URL = 'https://fragdenstaat.de'

    TASTYPIE_DEFAULT_FORMATS = ['json']
