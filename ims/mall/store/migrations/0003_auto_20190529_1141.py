# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-05-29 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=' ', upload_to='webpage/image'),
        ),
    ]
