# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-11 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0105_turma_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='disciplina',
            field=models.ManyToManyField(related_name='disciplinas', to='portal.Disciplina'),
        ),
    ]