# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-30 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_address_table',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
