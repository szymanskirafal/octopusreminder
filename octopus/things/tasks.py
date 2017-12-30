from django.core.mail import send_mail

from celery import shared_task
from celery.schedules import crontab







@shared_task
def task_send_email():
    send_mail('Octopus', 'Trying again celery and mailgun', 'octopus@octopusreminder.com', ['r.szymansky@gmail.com'])
