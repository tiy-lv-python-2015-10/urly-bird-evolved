# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0003_bookmark_bookmark_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='bookmark_hash',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
    ]
