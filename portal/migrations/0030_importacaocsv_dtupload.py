# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-27 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0029_importacaocsv_stimportacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='importacaocsv',
            name='dtupload',
            field=models.DateField(null=True),
        ),
    ]
