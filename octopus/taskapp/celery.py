from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.apps import apps, AppConfig
from django.conf import settings





if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # pragma: no cover


app = Celery('octopus')


class CeleryConfig(AppConfig):
    name = 'octopus.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object('django.conf:settings')
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # pragma: no cover

from celery.schedules import crontab
app.conf.beat_schedule = {
    'send-list-of-things-to-remember': {
        'task': 'octopus.things.tasks.task_send_email',
        'schedule': crontab(minute='0', hour='6,11,14,19'),


    },
}
