# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-18 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounters',
            name='whaler',
        ),
        migrations.RemoveField(
            model_name='administrators',
            name='viewer',
        ),
    ]