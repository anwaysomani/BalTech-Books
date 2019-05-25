# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-25 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products_table',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cgst_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sgst_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('igst_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('post_tax_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('launch_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='refill_request_table',
            fields=[
                ('refill_request_id', models.IntegerField(primary_key=True, serialize=False)),
                ('request_quantity', models.IntegerField()),
                ('request_date', models.DateTimeField(auto_now=True)),
                ('request_status', models.CharField(max_length=10)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer_table')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.products_table')),
            ],
        ),
        migrations.CreateModel(
            name='stock_entry_table',
            fields=[
                ('stock_entry_id', models.IntegerField(primary_key=True, serialize=False)),
                ('refill_quantity', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.products_table')),
            ],
        ),
        migrations.CreateModel(
            name='stock_table',
            fields=[
                ('stock_id', models.IntegerField(primary_key=True, serialize=False)),
                ('total_production_quantity', models.IntegerField()),
                ('current_quantity', models.IntegerField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.products_table')),
            ],
        ),
    ]
