# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-15 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0118_notasfaltas'),
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