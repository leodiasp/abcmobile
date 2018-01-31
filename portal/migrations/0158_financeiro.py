# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-24 18:12
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0157_auto_20180124_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=10)),
                ('parcela', models.CharField(max_length=5)),
                ('historico', models.TextField()),
                ('dtemissao', models.DateField()),
                ('vlr_titulo', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('dtbaixa', models.DateField()),
                ('vlr_baixa', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=4)),
                ('vlr_juros', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=4)),
                ('vlr_desconto', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=4)),
                ('periodoletivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.PeriodoLetivo')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Responsavel')),
            ],
        ),
    ]