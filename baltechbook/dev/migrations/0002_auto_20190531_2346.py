# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-31 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request_service_table',
            options={'verbose_name': 'Service Request', 'verbose_name_plural': 'Service Requests'},
        ),
    ]
