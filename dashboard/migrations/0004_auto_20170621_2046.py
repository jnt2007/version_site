# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-21 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170621_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powermaxversion',
            name='comment',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
