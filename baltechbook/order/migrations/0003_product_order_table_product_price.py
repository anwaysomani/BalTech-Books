# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-31 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190531_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_order_table',
            name='product_price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]