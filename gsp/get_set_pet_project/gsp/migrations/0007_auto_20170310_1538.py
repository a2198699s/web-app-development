# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsp', '0006_auto_20170308_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='-', unique=True),
            preserve_default=False,
        ),
    ]
