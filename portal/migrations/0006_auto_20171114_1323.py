# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-14 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20171114_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estado',
            old_name='estado_ibge',
            new_name='cd_ibge',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='estado_nome',
            new_name='nm_nome',
        ),
        migrations.RenameField(
            model_name='estado',
            old_name='estado_uf',
            new_name='sg_uf',
        ),
    ]
