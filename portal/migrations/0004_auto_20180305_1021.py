# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-05 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20180302_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensagem',
            old_name='dtalerta',
            new_name='dtmensagem',
        ),
    ]
