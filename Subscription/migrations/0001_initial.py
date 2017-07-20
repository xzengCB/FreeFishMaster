# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-20 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDT', models.DateTimeField(auto_now_add=True)),
                ('modifiedDT', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnalysisItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDT', models.DateTimeField(auto_now_add=True)),
                ('modifiedDT', models.DateTimeField(auto_now_add=True)),
                ('analysisID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subscription.Analysis')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('link', models.CharField(max_length=512)),
                ('imgLink', models.CharField(max_length=512)),
                ('modifiedDT', models.DateTimeField(auto_now_add=True)),
                ('createdDT', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=200)),
                ('priceLow', models.FloatField(default=0)),
                ('priceHigh', models.FloatField()),
                ('createdDT', models.DateTimeField(auto_now_add=True)),
                ('modifiedDT', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='analysisitem',
            name='itemID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subscription.Item'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='subscriptionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subscription.Subscription'),
        ),
    ]