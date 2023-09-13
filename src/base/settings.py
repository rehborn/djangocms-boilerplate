from pathlib import Path

from django.utils.translation import gettext_lazy as _

from .config import config, env, DEBUG, APP_DIR


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("secret_key")

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'modeltranslation',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'compressor',
    'base',
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'mptt',
    'djangocms_text_ckeditor',
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
]

plugins = config("plugins")
if plugins:
    for plugin in plugins:
        INSTALLED_APPS.append(f'cms_{plugin}')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
]

if not DEBUG:
    MIDDLEWARE.append('django.middleware.cache.FetchFromCacheMiddleware')

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', APP_DIR / 'config' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
                'base.context_processors.context_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/


USE_TZ = True
TIME_ZONE = 'UTC'
if config('timezone'):
    TIME_ZONE = config('timezone')

# Static Files
STATICFILES_DIRS = [
    APP_DIR / 'config' / 'static',
    APP_DIR / 'node_modules',
    BASE_DIR / 'static',
]


STATIC_URL = 'static/'
STATIC_ROOT = APP_DIR / "static"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),

)

# Media
MEDIA_URL = "media/"
MEDIA_ROOT = APP_DIR / "media"

SITE_ID = 1

X_FRAME_OPTIONS = 'SAMEORIGIN'

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

# languages
USE_I18N = True
LOCALE_PATHS = [BASE_DIR / "locales"]
LANGUAGES = [('en', 'English')]

if config('languages'):
    LANGUAGES = [(locale, _(locale)) for locale in config('languages')]

LANGUAGE_CODE = LANGUAGES[0][0]
MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE

CMS_LANGUAGES = {
    1: [{'code': lang[0], 'name': lang[0], 'public': True} for lang in LANGUAGES],
    'default': {
        'fallbacks': [LANGUAGES[0][0]],
        'redirect_on_fallback': False,
        'public': True,
        'hide_untranslated': True,
    },
}

# CMS Page Templates
CMS_TEMPLATES = [
    ('default.html', 'Default'),
    ('single-page.html', '[Special] Combine Sub Pages into a Single Page'),
]

if config('templates'):
    for template, descr in config('templates').items():
        CMS_TEMPLATES.append((f"{template}.html", f"{descr}"))


# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#         },
#     },
# }

# optional: enable sentry
if config('sentry_dsn'):
    import sentry_sdk

    sentry_sdk.init(
        dsn=config('sentry_dsn'),
        traces_sample_rate=1.0,
    )

# DjangoCMS Plugins
DJANGOCMS_PICTURE_TEMPLATES = [
    ('background', _('Background image')),
]
