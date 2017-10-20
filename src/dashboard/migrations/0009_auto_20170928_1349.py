# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20170801_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPMPVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=30)),
                ('comment', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='powermaxversion',
            name='ipmp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.IPMPVersion'),
        ),
    ]