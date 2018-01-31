# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-29 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0043_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('abreviacao', models.CharField(max_length=30)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao')),
            ],
        ),
    ]
