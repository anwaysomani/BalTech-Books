# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-25 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_service_table',
            name='webpage_ref',
            field=models.CharField(choices=[(b'Dashboard', b'Dashboard'), (b'Invoice', b'Invoice'), (b'Customers', b'Customers'), (b'Manage Orders', b'Manage Orders'), (b'Inventory', b'Inventory'), (b'Team', b'Team')], max_length=18),
        ),
    ]
