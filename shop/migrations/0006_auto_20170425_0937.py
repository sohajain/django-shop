# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170425_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='page_num',
            field=models.IntegerField(blank=True, default=None, verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, default=None, verbose_name='Год'),
        ),
    ]
