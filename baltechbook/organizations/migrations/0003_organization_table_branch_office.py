# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-01 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20190531_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization_table',
            name='branch_office',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]