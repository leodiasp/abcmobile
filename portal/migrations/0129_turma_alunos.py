# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-16 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0128_remove_disciplina_alunos'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='alunos',
            field=models.ManyToManyField(related_name='alunos', to='portal.Aluno'),
        ),
    ]