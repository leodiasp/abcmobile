# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-14 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_instituicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituicao',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='instituicao',
            name='estado',
        ),
        migrations.DeleteModel(
            name='Instituicao',
        ),
    ]