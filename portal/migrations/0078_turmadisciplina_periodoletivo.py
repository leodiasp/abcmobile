# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-27 16:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0077_auto_20171207_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='turmadisciplina',
            name='periodoletivo',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='portal.PeriodoLetivo'),
            preserve_default=False,
        ),
    ]
