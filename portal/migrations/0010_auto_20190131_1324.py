# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-31 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_aluno_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='imagem',
            field=models.FileField(blank=True, default='alunos/sem_foto.png', null=True, upload_to='alunos'),
        ),
    ]
