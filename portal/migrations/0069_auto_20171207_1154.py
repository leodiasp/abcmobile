# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-07 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0068_remove_turmadisciplina_aluno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turmadisciplina',
            name='periodoletivo',
        ),
        migrations.AddField(
            model_name='turmadisciplina',
            name='periodoletivo',
            field=models.ManyToManyField(to='portal.PeriodoLetivo'),
        ),
    ]
