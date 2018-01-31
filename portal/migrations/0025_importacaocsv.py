# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-24 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0024_remove_periodoletivo_arquivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportacaoCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tabela', models.CharField(max_length=100)),
                ('dtimportacao', models.DateField()),
                ('arquivo', models.FileField(upload_to=b'')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao')),
            ],
        ),
    ]
