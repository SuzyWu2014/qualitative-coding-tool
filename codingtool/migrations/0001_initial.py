# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('code_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.IntegerField()),
                ('is_partial', models.BooleanField(default=False)),
                ('is_emphasized', models.BooleanField(default=False)),
                ('has_many', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('explanation_id', models.AutoField(primary_key=True, serialize=False)),
                ('explanation', models.CharField(max_length=16)),
                ('source_link', models.URLField(max_length=256)),
                ('evernote_link', models.URLField(blank=True, max_length=256)),
                ('description', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goal_id', models.AutoField(primary_key=True, serialize=False)),
                ('goal', models.CharField(max_length=16)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notation',
            fields=[
                ('notation_id', models.AutoField(primary_key=True, serialize=False)),
                ('notation', models.CharField(max_length=16)),
                ('description', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=16)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='code',
            name='explanation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codingtool.Explanation'),
        ),
        migrations.AddField(
            model_name='code',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codingtool.Goal'),
        ),
        migrations.AddField(
            model_name='code',
            name='notations',
            field=models.ManyToManyField(to='codingtool.Notation'),
        ),
        migrations.AddField(
            model_name='code',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codingtool.Role'),
        ),
    ]
