# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-19 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('portal', '0149_imagemusuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemusuarios',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='ImagemUsuarios',
        ),
    ]