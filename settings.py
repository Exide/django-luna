import os

# Luna Settings

DEBUG = True
SITE_NAME = 'Luna'
ADMINS = ('Admin', 'admin@example.com')
# GOOGLE_ANALYTICS_KEY = 'UA-12345678-9'
ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.example.com'
EMAIL_HOST_USER = 'admin@example.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'

# Django specific settings below this line. Advanced users only!
# ----------------------------------------------------------------------------

TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
SECRET_KEY = 'you-should-generate-a-good-hash-for-this'
AUTHENTICATION_BACKENDS = 'account.backends.CaseInsensitiveBackend'
PAGINATION_DEFAULT_WINDOW = 5

ROOT_URLCONF = 'urls'
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

TEMPLATE_DIRS = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'account',
    'home',
    'forum',
    'games',
    'ventrilo',
    'registration',
    'tagging',
    'pagination',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'context_processors.default'
)
