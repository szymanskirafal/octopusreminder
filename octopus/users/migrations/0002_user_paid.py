# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-05 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
