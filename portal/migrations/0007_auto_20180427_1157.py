# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-27 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20180427_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='cidade',
            name='arquivo_importado',
            field=models.CharField(default=99, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado',
            name='arquivo_importado',
            field=models.CharField(default=99, max_length=200),
            preserve_default=False,
        ),
    ]