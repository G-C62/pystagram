# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 05:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20160804_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='status',
        ),
    ]
