# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-26 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0002_auto_20171126_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdata',
            name='default',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
