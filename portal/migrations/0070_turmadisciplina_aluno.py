# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-07 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0069_auto_20171207_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='turmadisciplina',
            name='aluno',
            field=models.ManyToManyField(to='portal.Aluno'),
        ),
    ]
