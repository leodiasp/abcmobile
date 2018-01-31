# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-15 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0124_auto_20180115_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notas', models.IntegerField()),
                ('faltas', models.IntegerField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Aluno')),
                ('disciplinas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Disciplina')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao')),
                ('periodoletivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.PeriodoLetivo')),
            ],
        ),
    ]
