# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsp', '0034_auto_20170324_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='ratings',
            field=models.ForeignKey(to='star_ratings.Rating'),
        ),
    ]
