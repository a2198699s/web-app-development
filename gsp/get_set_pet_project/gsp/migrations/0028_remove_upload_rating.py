# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-22 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsp', '0027_remove_userprofile_favourites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='rating',
        ),
    ]
