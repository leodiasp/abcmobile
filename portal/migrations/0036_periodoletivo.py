# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-29 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0035_auto_20171129_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodoLetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=60)),
                ('diasletivos', models.IntegerField()),
                ('dtinicial', models.DateField()),
                ('dtfinal', models.DateField()),
                ('calendario', models.CharField(max_length=16)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao')),
            ],
        ),
    ]
