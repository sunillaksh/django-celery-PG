from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

#  Celery Beat settings
app.conf.beat_schedule = {
    #  always crete new names not the same send-mail-every-day-at-8
    'send-mail-every-day-at-8': {
        'task': 'send_mail_app.task.send_mail_func',
        'schedule': crontab(hour=7,minute=38, day_of_month=19, month_of_year=6), }}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

    

