# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-17 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_auto_20171117_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens'),
        ),
    ]
