# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-15 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0120_notasfaltas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notasfaltas',
            name='disciplinas',
        ),
    ]