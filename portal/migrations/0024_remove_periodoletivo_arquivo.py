# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-24 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0023_periodoletivo_arquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodoletivo',
            name='arquivo',
        ),
    ]