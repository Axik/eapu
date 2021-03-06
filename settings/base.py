import os
import dj_database_url
from unipath import Path

PROJECT_DIR = Path()


def rel(*x):
    return PROJECT_DIR.child(*x)

os.sys.path.insert(0, rel('apps'))

DOMAIN = 'eapu.steelkiwi.com'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL', {}))}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'eapu'
    }
}

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Europe/Kiev'

LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = rel('public', 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = rel('public', 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    rel('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'hi5im@(ql6671yd=6u+_@!0+*+e)#*1_*h46ro)i)^v@^&66*v'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'common.urls'

WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    rel('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

# User settings
AUTH_USER_MODEL = 'auth.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/profile/'

LOG_FILE = rel('logs', 'app.log')


def get_ckeditor_upload_path():
    path = MEDIA_ROOT.child('upload')
    not os.path.exists(path) and os.makedirs(path, 0775)
    return path

CKEDITOR_UPLOAD_PATH = get_ckeditor_upload_path()

from .apps import *
from .logging import *
try:
    from .local import *
except ImportError:
    pass
