# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-06 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0059_auto_20171205_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmadisciplina',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
