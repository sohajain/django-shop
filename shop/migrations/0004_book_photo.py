# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170425_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.FileField(blank=True, upload_to='', verbose_name='Фото'),
        ),
    ]