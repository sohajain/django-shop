# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, upload_to='cover/%Y-%m', verbose_name='Фото'),
        ),
    ]