# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-15 14:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0116_auto_20180115_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notasfaltas',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='notasfaltas',
            name='instituicao',
        ),
        migrations.RemoveField(
            model_name='notasfaltas',
            name='periodoletivo',
        ),
        migrations.DeleteModel(
            name='NotasFaltas',
        ),
    ]
