# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsp', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]