# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default='White title', max_length=20, verbose_name='Title'),
        ),
    ]
