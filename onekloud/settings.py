"""
Django settings for Onekloud project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)

# Adding system paths
import sys
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9gfi8y+so)y+51=b@xpfnnlkm9^g+#xgjnl%sycs_n!5y)pvnz'

# SECURITY WARNING: don't reveal this key!
HMAC_KEY = 'af9df61ea6dc9a73439794d9d46afe1e376ae9983255e85b46c83123478a233b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '37.139.24.123',
    'www.onekloud.com'
]

AUTH_USER_MODEL = 'accounts.User'

ADMINS = (
    ('Aldash Biibosunov', 'support@onekloud.com'),
)


# Django application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


# Third-party application definition
INSTALLED_APPS += (
    'south',
)


# Onekloud application definition
INSTALLED_APPS += (
    'onekloud.apps.accounts',
    'onekloud.apps.pages',
)


# Django middleware classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Django context processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)


ROOT_URLCONF = 'onekloud.urls'

WSGI_APPLICATION = 'onekloud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'onekloud',
        'USER': 'oneklouduser',
        'PASSWORD': 'vivendi89',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kuala_Lumpur'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, '../static/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'common_static'),
)


# Template directories
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)


# Email
EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'aldash@onekloud.com'

EMAIL_HOST_PASSWORD = 'Vivendi89!'

EMAIL_PORT = 587

EMAIL_USE_TLS = True


# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '../logs/error.log')
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True
        }
    }
}


# Dev settings
try:
    from onekloud.settings_local import *
except ImportError:
    pass


# Test settings
if 'test' in sys.argv:
    from onekloud.settings_test import *
