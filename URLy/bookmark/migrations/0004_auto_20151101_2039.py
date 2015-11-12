# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0003_auto_20151030_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='click',
            old_name='users',
            new_name='user',
        ),
    ]
