# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-02 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20180228_1354'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alertas',
            new_name='Mensagem',
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='imagem',
            field=models.ImageField(blank=True, default='instituicao/sem_foto.png', null=True, upload_to='instituicao'),
        ),
    ]
