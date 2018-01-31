# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-12 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0107_auto_20180111_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='disciplinas',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='turmas',
            field=models.ManyToManyField(related_name='disciplinas', to='portal.Turma'),
        ),
    ]
