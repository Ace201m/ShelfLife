# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 13:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0012_feed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_front_page',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='name',
        ),
    ]
