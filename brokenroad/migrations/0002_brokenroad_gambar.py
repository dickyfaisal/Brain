# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-10 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokenroad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brokenroad',
            name='gambar',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
