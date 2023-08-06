# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django
import logging

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "4oqf)&7*65wbgo#0s#ww=g^rl=b16_b+sacz9-3z$*08qhea=7"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    'django_apscheduler',
    "django_db_log",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()


# LOOKUP DAYS TO DELETE OLD LOGS
INTERVAL_SCHEDULER_JOB_SECONDS = 43200
GENERAL_LOGS_DELETE_DAYS = 2
INFO_LOGS_DELETE_DAYS = 2
DEBUG_LOGS_DELETE_DAYS = 2
ERROR_LOGS_DELETE_DAYS = 10
