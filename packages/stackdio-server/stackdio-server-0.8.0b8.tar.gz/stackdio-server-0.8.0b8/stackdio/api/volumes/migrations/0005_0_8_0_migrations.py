# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-14 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volumes', '0004_0_8_0_migrations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volume',
            name='volume_id',
            field=models.CharField(blank=True, max_length=64, verbose_name='Volume ID'),
        ),
    ]
