# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-24 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190524_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_table',
            name='is_user',
            field=models.NullBooleanField(),
        ),
    ]