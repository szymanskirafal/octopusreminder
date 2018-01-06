from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from celery import shared_task
from celery.schedules import crontab

from .models import Thing
from ..users.models import User






@shared_task
def task_send_email():
    user = User.objects.get(email = 'szymanski_rafal@icloud.com')
    list_of_things = Thing.objects.all().filter(created_by = user)
    subject = 'List of things to remember'
    html_content = render_to_string('templates/things/email.html', {'things': list_of_things})
    from_email = 'octopus@octopusreminder.com'
    to = 'r.szymansky@gmail.com'
    email = EmailMessage(subject, html_content, from_email, [to])
    email.content_subtype = "html"
    email.send()

    #send_mail('Octopus', 'Trying again celery and mailgun', 'octopus@octopusreminder.com', ['r.szymansky@gmail.com'])
