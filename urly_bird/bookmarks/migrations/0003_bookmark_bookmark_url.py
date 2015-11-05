# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20151101_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='bookmark_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
