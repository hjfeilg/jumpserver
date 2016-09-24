# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-24 02:14
from __future__ import unicode_literals

import common.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('private_for', models.CharField(blank=True, choices=[('N', 'None'), ('U', 'user'), ('G', 'user group')], default='N', max_length=1, verbose_name='Private for')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_expired', models.DateTimeField(default=common.utils.date_expired_default, verbose_name='Date expired')),
                ('created_by', models.CharField(blank=True, max_length=128, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Date created')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('asset_groups', models.ManyToManyField(blank=True, related_name='granted_by_permissions', to='assets.AssetGroup')),
                ('assets', models.ManyToManyField(blank=True, related_name='granted_by_permissions', to='assets.Asset')),
                ('system_users', models.ManyToManyField(related_name='granted_by_permissions', to='assets.SystemUser')),
            ],
            options={
                'db_table': 'asset_permission',
            },
        ),
    ]
