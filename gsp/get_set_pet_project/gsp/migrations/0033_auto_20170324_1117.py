# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-24 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gsp', '0032_auto_20170324_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='ratings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='star_ratings.Rating'),
        ),
    ]
