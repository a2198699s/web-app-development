# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gsp', '0033_auto_20170324_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='ratings',
            field=models.ForeignKey(related_query_name='uploads', to='star_ratings.Rating'),
        ),
    ]
