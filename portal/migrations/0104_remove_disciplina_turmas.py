# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-11 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0103_auto_20180111_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='turmas',
        ),
    ]