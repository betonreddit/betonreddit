# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(default='guest', max_length=12),
        ),
    ]