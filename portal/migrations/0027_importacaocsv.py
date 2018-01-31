# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-24 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0026_auto_20171124_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportacaoCSV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtimportacao', models.DateField()),
                ('arquivo', models.FileField(upload_to=b'')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Instituicao')),
                ('tabelaimportacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.TabelaImportacao')),
            ],
        ),
    ]