# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-04 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0085_remove_disciplina_instituicao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boletim',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='boletim',
            name='instituicao',
        ),
        migrations.RemoveField(
            model_name='boletim',
            name='periodoletivo',
        ),
        migrations.RemoveField(
            model_name='boletim',
            name='turmadisciplina',
        ),
        migrations.RemoveField(
            model_name='turmadisciplina',
            name='instituicao',
        ),
        migrations.RemoveField(
            model_name='turmadisciplina',
            name='periodoletivo',
        ),
        migrations.DeleteModel(
            name='Boletim',
        ),
        migrations.DeleteModel(
            name='TurmaDisciplina',
        ),
    ]
