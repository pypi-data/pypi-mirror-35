# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import url

app_name = 'django_db_log'
urlpatterns = [
    url(r'admin/', admin.site.urls),
]
