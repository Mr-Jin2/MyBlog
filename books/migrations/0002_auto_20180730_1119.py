# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-30 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.CharField(default='i am jing', max_length=200),
        ),
    ]