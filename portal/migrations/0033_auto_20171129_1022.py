# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-29 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0032_auto_20171127_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodoletivo',
            name='id',
        ),
        migrations.AlterField(
            model_name='periodoletivo',
            name='codigo',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
