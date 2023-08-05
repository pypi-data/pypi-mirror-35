# -*- coding: utf-8 -*-
import json
import os
import sys
import django_cache_url
import dj_database_url
import dj_email_url

import warnings
from functools import partial
from django_addons.utils import boolean_ish, djsenv

import yurl


class CachedLoader(list):
    """
    A list subclass to be used for the template loaders option

    This subclass exposes the same interface as a list and allows subsequent
    code to alter the list of template loaders without knowing if it has been
    wrapped by the `django.template.loaders.cached.Loader` loader.

    `uncached_*` methods are available to allow cached-loader-aware code to
    alter the main template loaders.
    """
    loader = 'django.template.loaders.cached.Loader'

    def __init__(self, loaders):
        self._cached_loaders = list(loaders)
        super(CachedLoader, self).__init__([
            (self.loader, self._cached_loaders),
        ])

        methods = ('append', 'extend', 'insert', 'remove',
                   'pop', 'index', 'count')
        for method in methods:
            self.overwrite_method(method)

    def overwrite_method(self, method):
        uncached_method = 'uncached_{}'.format(method)
        setattr(self, uncached_method, getattr(self, method))
        setattr(self, method, getattr(self._cached_loaders, method))


class Config():
    def __call__(self, formdata, settings):
        self.env = env = partial(djsenv, settings=settings)
        self.formdata = formdata
        self.settings = settings
        # BASE_DIR should already be set by aldryn-addons
        settings['BASE_DIR'] = env('BASE_DIR', required=True)
        settings['DATA_ROOT'] = env('DATA_ROOT', os.path.join(settings['BASE_DIR'], 'data'))
        settings['SECRET_KEY'] = env('SECRET_KEY', 'this-is-not-very-random')
        settings['DEBUG'] = boolean_ish(env('DEBUG', False))
        settings['ENABLE_SYNCING'] = boolean_ish(
            env('ENABLE_SYNCING', settings['DEBUG']))
        settings['DISABLE_TEMPLATE_CACHE'] = boolean_ish(
            env('DISABLE_TEMPLATE_CACHE', settings['DEBUG']))

        settings['DATABASE_URL'] = env('DATABASE_URL')
        settings['CACHE_URL'] = env('CACHE_URL')
        if env('DJANGO_MODE') == 'build':
            # In build mode we don't have any connected services like db or
            # cache available. So we need to configure those things in a way
            # they can run without real backends.
            settings['DATABASE_URL'] = 'sqlite://:memory:'
            settings['CACHE_URL'] = 'locmem://'

        if not settings['DATABASE_URL']:
            settings['DATABASE_URL'] = 'sqlite:///{}'.format(
                os.path.join(settings['DATA_ROOT'], 'db.sqlite3')
            )
            warnings.warn(
                'no database configured. Falling back to DATABASE_URL={0}'.format(
                    settings['DATABASE_URL']
                ),
                RuntimeWarning,
            )
        settings['DATABASES']['default'] = dj_database_url.parse(settings['DATABASE_URL'])

        if not settings['CACHE_URL']:
            settings['CACHE_URL'] = 'locmem://'
            warnings.warn(
                'no cache configured. Falling back to CACHE_URL={0}'.format(
                    settings['CACHE_URL']
                ),
                RuntimeWarning,
            )
        settings['CACHES']['default'] = django_cache_url.parse(settings['CACHE_URL'])

        settings['ROOT_URLCONF'] = env('ROOT_URLCONF', 'urls')
        settings['ADDON_URLS_I18N'].append('django_addon.i18n_urls')

        settings['WSGI_APPLICATION'] = 'wsgi.application'

        settings['INSTALLED_APPS'].extend([
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.admin',
            'django.contrib.staticfiles',
            'django_addon',
        ])

        if settings['ENABLE_SYNCING'] or settings['DISABLE_TEMPLATE_CACHE']:
            loader_list_class = list
        else:
            loader_list_class = CachedLoader

        settings['TEMPLATES'] = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': env('TEMPLATE_DIRS', [os.path.join(settings['BASE_DIR'], 'templates')], ),
                'OPTIONS': {
                    'debug': boolean_ish(env('TEMPLATE_DEBUG', settings['DEBUG'])),
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                        'django.template.context_processors.i18n',
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.template.context_processors.media',
                        'django.template.context_processors.csrf',
                        'django.template.context_processors.tz',
                        'django.template.context_processors.static',
                        'django_addon.context_processors.debug',
                    ],
                    'loaders': loader_list_class([
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ]),
                },
            },
        ]

        settings['MIDDLEWARE'] = [
            'django.middleware.security.SecurityMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            'django.contrib.sites.middleware.CurrentSiteMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

        if not env('DISABLE_GZIP'):
            settings['MIDDLEWARE'].insert(
                0, 'django.middleware.gzip.GZipMiddleware')

        settings['SITE_ID'] = env('SITE_ID', 1)

        settings['ADDON_URLS_I18N_LAST'] = 'django_addon.urls_redirect'

        self.domain_settings()
        self.security_settings()
        self.server_settings()
        self.logging_settings()
        # Order matters, sentry settings rely on logging being configured.
        self.sentry_settings()
        self.storage_settings_for_media()
        self.storage_settings_for_static()
        self.email_settings()
        self.i18n_settings()
        self.migration_settings()
        settings['DJANGO_ADDON_ENABLE_GIS'] = formdata['enable_gis']
        if settings['DJANGO_ADDON_ENABLE_GIS']:
            self.gis_settings()

    def domain_settings(self):
        env = self.env
        settings = self.settings
        formdata = self.formdata
        settings['ALLOWED_HOSTS'] = env('ALLOWED_HOSTS', ['localhost', '*'])
        # will take a full config dict from ALDRYN_SITES_DOMAINS if available,
        # otherwise fall back to constructing the dict from DOMAIN,
        # DOMAIN_ALIASES and DOMAIN_REDIRECTS
        domain = env('DOMAIN')
        if domain:
            settings['DOMAIN'] = domain

        domains = env('ALDRYN_SITES_DOMAINS', {})
        if not domains and domain:
            domain_aliases = [
                d.strip()
                for d in env('DOMAIN_ALIASES', '').split(',')
                if d.strip()
            ]
            domain_redirects = [
                d.strip()
                for d in env('DOMAIN_REDIRECTS', '').split(',')
                if d.strip()
            ]
            domains = {
                1: {
                    'name': env('SITE_NAME', ''),
                    'domain': domain,
                    'aliases': domain_aliases,
                    'redirects': domain_redirects,
                },
            }
        settings['ALDRYN_SITES_DOMAINS'] = domains

        # This is ensured again by aldryn-sites, but we already do it here
        # as we need the full list of domains later when configuring
        # media/static serving, before aldryn-sites had a chance to run.
        site_domains = domains.get(settings['SITE_ID'])
        if site_domains:
            settings['ALLOWED_HOSTS'].append(site_domains['domain'])
            settings['ALLOWED_HOSTS'].extend(site_domains['aliases'])
            settings['ALLOWED_HOSTS'].extend(site_domains['redirects'])

        settings['INSTALLED_APPS'].append('aldryn_sites')

        settings['MIDDLEWARE'].insert(
            settings['MIDDLEWARE'].index('django.middleware.common.CommonMiddleware'),
            'aldryn_sites.middleware.SiteMiddleware',
        )

    def security_settings(self):
        env = self.env
        s = self.settings
        formdata = self.formdata
        s['SECURE_SSL_REDIRECT'] = env('SECURE_SSL_REDIRECT', None)
        s['SECURE_REDIRECT_EXEMPT'] = env('SECURE_REDIRECT_EXEMPT', [])
        s['SECURE_HSTS_SECONDS'] = env('SECURE_HSTS_SECONDS', 0)
        # SESSION_COOKIE_SECURE is handled by
        #   django.contrib.sessions.middleware.SessionMiddleware
        s['SESSION_COOKIE_SECURE'] = env('SESSION_COOKIE_SECURE', False)
        s['SECURE_PROXY_SSL_HEADER'] = env(
            'SECURE_PROXY_SSL_HEADER',
            ('HTTP_X_FORWARDED_PROTO', 'https')
        )
        s['SESSION_COOKIE_AGE'] = env('SESSION_COOKIE_AGE', formdata.get('session_timeout') or 60 * 60 * 24 * 7 * 2)

        # SESSION_COOKIE_HTTPONLY and SECURE_FRAME_DENY must be False for CMS
        # SESSION_COOKIE_HTTPONLY is handled by
        #   django.contrib.sessions.middleware.SessionMiddleware
        s['SESSION_COOKIE_HTTPONLY'] = env('SESSION_COOKIE_HTTPONLY', False)

        s['SECURE_CONTENT_TYPE_NOSNIFF'] = env('SECURE_CONTENT_TYPE_NOSNIFF', False)
        s['SECURE_BROWSER_XSS_FILTER'] = env('SECURE_BROWSER_XSS_FILTER', False)

        s['MIDDLEWARE'].insert(
            s['MIDDLEWARE'].index('aldryn_sites.middleware.SiteMiddleware') + 1,
            'django.middleware.security.SecurityMiddleware',
        )

    def server_settings(self):
        env = self.env
        settings = self.settings
        settings['PORT'] = env('PORT', 80)
        settings['BACKEND_PORT'] = env('BACKEND_PORT', 8000)
        settings['ENABLE_NGINX'] = env('ENABLE_NGINX', False)
        settings['ENABLE_PAGESPEED'] = env(
            'ENABLE_PAGESPEED',
            env('PAGESPEED', False),
        )
        settings['STATICFILES_DEFAULT_MAX_AGE'] = env(
            'STATICFILES_DEFAULT_MAX_AGE',
            # Keep BROWSERCACHE_MAX_AGE for backwards compatibility
            env('BROWSERCACHE_MAX_AGE', 300),
        )
        settings['NGINX_CONF_PATH'] = env('NGINX_CONF_PATH')
        settings['NGINX_PROCFILE_PATH'] = env('NGINX_PROCFILE_PATH')
        settings['PAGESPEED_ADMIN_HTPASSWD_PATH'] = env(
            'PAGESPEED_ADMIN_HTPASSWD_PATH',
            os.path.join(
                os.path.dirname(settings['NGINX_CONF_PATH']),
                'pagespeed_admin.htpasswd',
            )
        )
        settings['PAGESPEED_ADMIN_USER'] = env('PAGESPEED_ADMIN_USER')
        settings['PAGESPEED_ADMIN_PASSWORD'] = env('PAGESPEED_ADMIN_PASSWORD')
        settings['DJANGO_WEB_WORKERS'] = env('DJANGO_WEB_WORKERS', 3)
        settings['DJANGO_WEB_MAX_REQUESTS'] = env('DJANGO_WEB_MAX_REQUESTS', 500)
        settings['DJANGO_WEB_TIMEOUT'] = env('DJANGO_WEB_TIMEOUT', 120)

        # https://docs.djangoproject.com/en/1.8/ref/settings/#use-x-forwarded-host
        settings['USE_X_FORWARDED_HOST'] = env('USE_X_FORWARDED_HOST', False)

    def logging_settings(self):
        env = self.env
        settings = self.settings
        formdata = self.formdata
        settings['LOGGING'] = {
            'version': 1,
            'disable_existing_loggers': False,
            'filters': {
                'require_debug_false': {
                    '()': 'django.utils.log.RequireDebugFalse',
                },
                'require_debug_true': {
                    '()': 'django.utils.log.RequireDebugTrue',
                },
            },
            'handlers': {
                'console': {
                    'level': 'INFO',
                    'class': 'logging.StreamHandler',
                    'stream': sys.stdout,
                },
                'null': {
                    'class': 'logging.NullHandler',
                },
            },
            'loggers': {
                '': {
                    'handlers': ['console'],
                    'level': 'INFO',
                },
                'django': {
                    'handlers': ['console'],
                    'level': 'INFO',
                },
                'django.request': {
                    'handlers': ['console'],
                    'level': 'INFO',
                    'propagate': False,
                },
                'aldryn': {
                    'handlers': ['console'],
                    'level': 'INFO',
                },
                'py.warnings': {
                    'handlers': ['console'],
                },
            }
        }

    def sentry_settings(self):
        env = self.env
        settings = self.settings
        sentry_dsn = env('SENTRY_DSN')

        if sentry_dsn:
            settings['INSTALLED_APPS'].append('raven.contrib.django')
            settings['RAVEN_CONFIG'] = {'dsn': sentry_dsn}
            settings['LOGGING']['handlers']['sentry'] = {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            }

    def storage_settings_for_media(self):
        from django_addon.storage import parse_storage_url
        env = self.env
        settings = self.settings

        if env('DEFAULT_STORAGE_DSN'):
            settings['DEFAULT_STORAGE_DSN'] = env('DEFAULT_STORAGE_DSN')
        settings['MEDIA_URL'] = env('MEDIA_URL', '/media/')
        if 'DEFAULT_STORAGE_DSN' in settings:
            settings.update(parse_storage_url(settings['DEFAULT_STORAGE_DSN']))
        media_host = yurl.URL(settings['MEDIA_URL']).host
        settings['MEDIA_URL_IS_ON_OTHER_DOMAIN'] = (
            media_host and media_host not in settings['ALLOWED_HOSTS']
        )
        settings['MEDIA_ROOT'] = env('MEDIA_ROOT', os.path.join(settings['DATA_ROOT'], 'media'))
        settings['MEDIA_HEADERS'] = []

        cmds = {}
        if os.path.exists('/usr/bin/pngout'):
            cmds['png'] = '/usr/bin/pngout {filename} {filename}.png -s0 -y -force && mv {filename}.png {filename}'
        if os.path.exists('/usr/bin/jpegoptim'):
            cmds['jpeg'] = '/usr/bin/jpegoptim --max=90 --overwrite --strip-all --all-progressive {filename}'
        if os.path.exists('/usr/bin/gifsicle'):
            cmds['gif'] = '/usr/bin/gifsicle --batch --optimize=2 {filename}'
        settings['THUMBNAIL_OPTIMIZE_COMMAND'] = cmds

    def storage_settings_for_static(self):
        env = self.env
        settings = self.settings
        formdata = self.formdata

        use_gzip = not env('DISABLE_GZIP')
        use_manifest = formdata['use_manifeststaticfilesstorage']
        if use_gzip:
            if use_manifest:
                storage = 'django_addon.storage.ManifestGZippedStaticFilesStorage'
            else:
                storage = 'django_addon.storage.GZippedStaticFilesStorage'
        else:
            if use_manifest:
                storage = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
            else:
                storage = 'django.contrib.staticfiles.storage.StaticFilesStorage'
        settings['STATICFILES_STORAGE'] = storage

        settings['STATIC_URL'] = env('STATIC_URL', '/static/')
        static_host = yurl.URL(settings['STATIC_URL']).host
        settings['STATIC_URL_IS_ON_OTHER_DOMAIN'] = (
            static_host and static_host not in settings['ALLOWED_HOSTS']
        )
        settings['STATIC_ROOT'] = env(
            'STATIC_ROOT',
            os.path.join(settings['BASE_DIR'], 'static_collected'),
        )
        settings['STATIC_HEADERS'] = [
            # Set far-future expiration headers for static files with hashed
            # filenames. Also set cors headers to * for fonts.
            (r'.*\.[0-9a-f]{10,16}\.(eot|ttf|otf|woff)', {
                'Access-Control-Allow-Origin': '*',
                'Cache-Control': 'public, max-age={}'.format(3600 * 24 * 365),
            }),
            (r'.*\.[0-9a-f]{10,16}\.[a-z]+', {
                'Cache-Control': 'public, max-age={}'.format(3600 * 24 * 365),
            }),
            # Set default expiration headers for all remaining static files.
            # *Has to be last* as processing stops at the first matching
            # pattern it finds. Also set cors headers to * for fonts.
            (r'.*\.(eot|ttf|otf|woff)', {
                'Access-Control-Allow-Origin': '*',
                'Cache-Control': 'public, max-age={}'.format(
                    settings['STATICFILES_DEFAULT_MAX_AGE'],
                ),
            }),
            ('.*', {
                'Cache-Control': 'public, max-age={}'.format(
                    settings['STATICFILES_DEFAULT_MAX_AGE'],
                ),
            }),
        ]
        settings['STATICFILES_DIRS'] = env(
            'STATICFILES_DIRS',
            [os.path.join(settings['BASE_DIR'], 'static')]
        )

    def email_settings(self):
        env = self.env
        settings = self.settings

        email_url = env('EMAIL_URL', '')
        if email_url:
            settings['EMAIL_URL'] = email_url
            settings.update(dj_email_url.parse(email_url))

        from_email = env('DEFAULT_FROM_EMAIL', '')
        if from_email:
            settings['DEFAULT_FROM_EMAIL'] = from_email

        server_email = env('SERVER_EMAIL', '')
        if server_email:
            settings['SERVER_EMAIL'] = server_email

    def i18n_settings(self):
        env = self.env
        settings = self.settings
        formdata = self.formdata

        settings['ALL_LANGUAGES'] = list(settings['LANGUAGES'])
        settings['ALL_LANGUAGES_DICT'] = dict(settings['ALL_LANGUAGES'])

        settings['USE_L10N'] = True
        settings['USE_I18N'] = True

        def language_codes_to_tuple(codes):
            return [
                (code, settings['ALL_LANGUAGES_DICT'][code])
                for code in codes
            ]
        langs_from_env = env('LANGUAGES', None)
        lang_codes_from_env = env('LANGUAGE_CODES', None)
        langs_from_form = json.loads(formdata['languages'])

        if langs_from_env:
            settings['LANGUAGES'] = langs_from_env
        elif lang_codes_from_env:
            settings['LANGUAGES'] = language_codes_to_tuple(lang_codes_from_env)
        else:
            settings['LANGUAGES'] = language_codes_to_tuple(langs_from_form)

        lang_code_from_env = env('LANGUAGE_CODE', None)
        if lang_code_from_env:
            settings['LANGUAGE_CODE'] = lang_code_from_env
        else:
            settings['LANGUAGE_CODE'] = settings['LANGUAGES'][0][0]

        settings['LOCALE_PATHS'] = [
            os.path.join(settings['BASE_DIR'], 'locale'),
        ]
        settings['PREFIX_DEFAULT_LANGUAGE'] = not formdata['disable_default_language_prefix']

        if not settings['PREFIX_DEFAULT_LANGUAGE']:
            settings['MIDDLEWARE'].insert(
                settings['MIDDLEWARE'].index('django.middleware.locale.LocaleMiddleware'),
                'django_addon.middleware.LanguagePrefixFallbackMiddleware',
            )

    def time_settings(self):
        env = self.env
        settings = self.settings

        if env('TIME_ZONE'):
            settings['TIME_ZONE'] = env('TIME_ZONE')

    def migration_settings(self):
        from . import storage
        env = self.env
        settings = self.settings

        settings.setdefault('MIGRATION_COMMANDS', [])
        mcmds = settings['MIGRATION_COMMANDS']

        mcmds.append('CACHE_URL="locmem://" python manage.py createcachetable django_dbcache; exit 0')
        mcmds.append('python manage.py migrate --noinput')

        if not boolean_ish(env('DISABLE_S3_MEDIA_HEADERS_UPDATE')):
            if settings['DEFAULT_FILE_STORAGE'] == storage.SCHEMES['s3']:
                mcmds.append('python manage.py aldryn_update_s3_media_headers')

    def gis_settings(self):
        settings = self.settings
        settings['DATABASES']['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
        settings['INSTALLED_APPS'].append('django.contrib.gis')


load = Config()
