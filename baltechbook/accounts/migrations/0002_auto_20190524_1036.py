# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-24 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_table',
            name='is_user',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]