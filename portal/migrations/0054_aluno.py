# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-04 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0053_auto_20171204_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro_aluno', models.CharField(max_length=20)),
                ('codigo', models.IntegerField()),
                ('nome', models.CharField(max_length=120)),
                ('nome_abreviado', models.CharField(max_length=40)),
                ('dtnascimento', models.DateField()),
                ('sexo', models.CharField(max_length=2)),
                ('cpf', models.CharField(max_length=20)),
                ('identidade', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('endereco', models.CharField(max_length=140)),
                ('complemento', models.CharField(max_length=60)),
                ('bairro', models.CharField(max_length=80)),
                ('cidade', models.CharField(max_length=60)),
                ('uf', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=20)),
                ('telefone2', models.CharField(max_length=20)),
                ('intituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao')),
            ],
        ),
    ]
