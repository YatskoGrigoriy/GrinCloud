# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-06 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20170706_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/blogimage', verbose_name='Ваше фото'),
        ),
    ]
