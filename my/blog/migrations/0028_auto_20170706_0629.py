# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-06 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20170706_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blogimage/', verbose_name='Ваше фото'),
        ),
    ]
