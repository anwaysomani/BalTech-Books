# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-21 12:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('country', models.CharField(max_length=75)),
                ('contactNumber', models.IntegerField()),
                ('emailAddress', models.EmailField(max_length=200)),
                ('webLink', models.URLField()),
                ('gstNo', models.CharField(max_length=15)),
                ('authorizedGeneral', models.CharField(max_length=100)),
                ('organizationLogo', models.ImageField(upload_to=b'')),
                ('totalOfficials', models.IntegerField()),
            ],
        ),
    ]