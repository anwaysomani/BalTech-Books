# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-01 16:14
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0002_auto_20190531_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='registered_shop',
            fields=[
                ('shop_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200, null=True)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[(b'Andhra Pradesh', b'Andhra Pradesh'), (b'Arunachal Pradesh', b'Arunachal Pradesh'), (b'Assam', b'Assam'), (b'Bihar', b'Bihar'), (b'Chattisgarh', b'Chattisgarh'), (b'Goa', b'Goa'), (b'Gujarat', b'Gujarat'), (b'Haryana', b'Haryana'), (b'Himachal Pradesh', b'Himachal Pradesh'), (b'Jammu and Kashmir', b'Jammu and Kashmir'), (b'Jharkhand', b'Jharkhand'), (b'Karnataka', b'Karnataka'), (b'Kerala', b'Kerala'), (b'Madhya Pradesh', b'Madhya Pradesh'), (b'Maharashtra', b'Maharashtra'), (b'Manipur', b'Manipur'), (b'Meghalaya', b'Meghalaya'), (b'Mizoram', b'Mizoram'), (b'Nagaland', b'Nagaland'), (b'Odisha', b'Odisha'), (b'Punjab', b'Punjab'), (b'Rajasthan', b'Rajasthan'), (b'Sikkim', b'Sikkim'), (b'Tamil Nadu', b'Tamil Nadu'), (b'Telangana', b'Telangana'), (b'Tripura', b'Tripura'), (b'Uttar Pradesh', b'Uttar Pradesh'), (b'Uttarakhand', b'Uttarakhand'), (b'West Bengal', b'West Bengal')], max_length=100)),
                ('country', models.CharField(choices=[(b'India', b'India')], max_length=100)),
                ('pincode', models.IntegerField(null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('employee_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
