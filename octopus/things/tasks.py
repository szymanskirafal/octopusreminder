from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from celery import shared_task
from celery.schedules import crontab

from .models import Thing
from ..users.models import User






@shared_task
def task_send_email():
    user = User.objects.get(username = 'szymanski')
    list_of_things = Thing.objects.all().filter(created_by = user)
    today_things = list_of_things.filter(today = True)
    later_things = list_of_things.filter(today = False)
    subject = 'List of things to remember'
    html_content = render_to_string('things/email.html', {'today_things': today_things, 'later_things': later_things})
    from_email = 'octopus@octopusreminder.com'
    to = 'r.szymansky@gmail.com'
    email = EmailMessage(subject, html_content, from_email, [to])
    email.content_subtype = "html"
    email.send()

    #send_mail('Octopus', 'Trying again celery and mailgun', 'octopus@octopusreminder.com', ['r.szymansky@gmail.com'])
