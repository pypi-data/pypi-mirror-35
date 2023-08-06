# -*- coding: utf-8
from django.apps import AppConfig


class DjangoDbLogConfig(AppConfig):
    name = 'django_db_log'
    verbose_name = 'Django DB Log'

    def ready(self):
        import tasks
