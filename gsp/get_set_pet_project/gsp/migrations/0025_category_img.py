# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-20 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsp', '0024_auto_20170320_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.CharField(default=0, max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
