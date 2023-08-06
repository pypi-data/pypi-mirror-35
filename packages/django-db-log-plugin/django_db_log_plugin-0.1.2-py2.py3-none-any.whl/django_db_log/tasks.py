from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django_db_log.models import GeneralLog, DebugLog, InfoLog, ErrorLog
from django.conf import settings

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


def get_time_threshold(days=10):
    return datetime.now() - timedelta(days=days)


@register_job(scheduler, "interval", seconds=settings.INTERVAL_SCHEDULER_JOB_SECONDS, id="general_log")
def delete_general_logs():
    GeneralLog.objects.filter(time__lt=get_time_threshold(days=settings.GENERAL_LOGS_DELETE_DAYS)).delete()


@register_job(scheduler, "interval", seconds=settings.INTERVAL_SCHEDULER_JOB_SECONDS, id="info_log")
def delete_info_logs():
    InfoLog.objects.filter(time__lt=get_time_threshold(days=settings.INFO_LOGS_DELETE_DAYS)).delete()


@register_job(scheduler, "interval", seconds=settings.INTERVAL_SCHEDULER_JOB_SECONDS, id="debug_log")
def delete_debug_logs():
    DebugLog.objects.filter(time__lt=get_time_threshold(days=settings.DEBUG_LOGS_DELETE_DAYS)).delete()


@register_job(scheduler, "interval", seconds=settings.INTERVAL_SCHEDULER_JOB_SECONDS, id="error_log")
def delete_error_logs():
    ErrorLog.objects.filter(time__lt=get_time_threshold(days=settings.ERROR_LOGS_DELETE_DAYS)).delete()


register_events(scheduler)

if not scheduler.running:
    scheduler.start()
    print("Scheduler started!")
