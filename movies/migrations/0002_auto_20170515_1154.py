# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='cast',
            field=models.TextField(),
        ),
    ]
