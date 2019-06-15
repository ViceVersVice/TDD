# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-12 18:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20190513_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='registration_number',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
