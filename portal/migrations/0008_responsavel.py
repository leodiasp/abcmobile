# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-28 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_delete_responsavel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('registro_responsavel', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=120)),
                ('cpf', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=60)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('imagem', models.ImageField(blank=True, default='responsavel/sem_foto.png', null=True, upload_to='responsavel')),
                ('arquivo_importado', models.CharField(max_length=200)),
            ],
        ),
    ]
