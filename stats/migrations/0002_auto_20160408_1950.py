# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
