# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Photo',
            new_name='photo',
        ),
    ]
