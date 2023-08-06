from __future__ import unicode_literals, absolute_import

import django
import os

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', ]
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_apscheduler',
    'django_db_log',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ROOT_URLCONF = "django_db_log.urls"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "4oqf)&7*65wbgo#0s#ww=g^rl=b16_b+sacz9-3z$*08qhea=7"

if django.VERSION >= (1, 10):
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
else:
    MIDDLEWARE_CLASSES = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
           'format': '[%(asctime)s] %(levelname)s %(module)s.%(funcName)s %(lineno)d: %(message)s'
        },
        'simple': {
            'format': ' %(levelname)s  %(message)s',
        },
    },
    'handlers': {
        'log_db': {
            'level': 'ERROR',
            'class': 'django_db_log.handlers.DBHandler',
            'model': 'django_db_log.models.ErrorLog',
            'expiry': 86400,
            # 'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['log_db'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_db_log', 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# LOOKUP DAYS TO DELETE OLD LOGS
INTERVAL_SCHEDULER_JOB_SECONDS = 43200
GENERAL_LOGS_DELETE_DAYS = 2
INFO_LOGS_DELETE_DAYS = 2
DEBUG_LOGS_DELETE_DAYS = 2
ERROR_LOGS_DELETE_DAYS = 10
