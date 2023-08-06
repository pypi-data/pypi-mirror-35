# -*- coding: utf-8 -*-
from django.db import models


class DatabaseLog(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10)
    message = models.TextField()

    class Meta:
        abstract = True
        verbose_name = 'System Log Entry'
        verbose_name_plural = 'System Log Entries'

    def __unicode__(self):
        return '{0} - {1}'.format(self.time, self.message[:100])


class GeneralLog(DatabaseLog):
    pass


class InfoLog(DatabaseLog):
    pass


class DebugLog(DatabaseLog):
    pass


class ErrorLog(DatabaseLog):
    pass
