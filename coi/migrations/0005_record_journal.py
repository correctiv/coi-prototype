# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coi', '0004_record_paper_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='journal',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
