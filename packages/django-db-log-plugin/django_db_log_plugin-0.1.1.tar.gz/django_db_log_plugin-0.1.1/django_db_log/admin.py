from django.contrib import admin
from .models import ErrorLog


class ErrorLogAdmin(admin.ModelAdmin):

    list_display = ['time', 'level', 'message']
    ordering = ['time', ]
    readonly_fields = ('time', 'level', 'message')


admin.site.register(ErrorLog, ErrorLogAdmin)
