# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-30 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170530_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.CharField(max_length=100, null=True, verbose_name='Видео'),
        ),
    ]
