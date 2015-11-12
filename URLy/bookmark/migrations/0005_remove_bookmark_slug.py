# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0004_auto_20151101_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='slug',
        ),
    ]
