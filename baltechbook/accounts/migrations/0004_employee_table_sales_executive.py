# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-01 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190601_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_table',
            name='sales_executive',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
