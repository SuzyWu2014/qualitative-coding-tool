# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codingtool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='description',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='explanation',
            name='description',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='explanation',
            name='evernote_link',
            field=models.URLField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='notation',
            name='description',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
