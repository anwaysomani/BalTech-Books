# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-21 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_accounters_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accounters',
            new_name='Accounter',
        ),
        migrations.RenameModel(
            old_name='Administrators',
            new_name='Administrator',
        ),
    ]