# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_url_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('link', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.RenameField(
            model_name='click',
            old_name='users',
            new_name='users',
        ),
        migrations.AlterField(
            model_name='click',
            name='bookmark',
            field=models.ForeignKey(to='bookmark.Bookmark'),
        ),
        migrations.DeleteModel(
            name='URL',
        ),
    ]
