# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-26 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20180426_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaosocial', models.CharField(max_length=100, null=True)),
                ('nomefantasia', models.CharField(max_length=100)),
                ('cgc', models.CharField(max_length=20)),
                ('inscestadual', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('telefax', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(max_length=60)),
                ('endereco', models.CharField(max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('bairro', models.CharField(max_length=80)),
                ('cep', models.CharField(max_length=10)),
                ('contato', models.CharField(max_length=40)),
                ('imagem', models.ImageField(blank=True, default='instituicao/sem_foto.png', null=True, upload_to='instituicao')),
                ('dtcadastro', models.DateField(auto_now=True)),
                ('numero_alunos', models.IntegerField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Cidade')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Estado')),
            ],
        ),
    ]