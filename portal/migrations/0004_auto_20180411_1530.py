# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-11 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20180321_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='sexo',
            field=models.CharField(max_length=10),
        ),
    ]
