# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-22 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20170622_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powermaxversion',
            name='kp_250',
            field=models.ForeignKey(blank=True, default='No Plink', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.KP250Version'),
        ),
    ]
