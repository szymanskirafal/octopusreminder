# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-05 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0007_auto_20180110_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaysOfFreeUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.PositiveSmallIntegerField()),
            ],
        ),
    ]