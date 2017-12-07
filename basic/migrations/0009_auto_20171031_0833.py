# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0008_auto_20171031_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='liked_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='album',
            name='posted_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='author',
            name='liked_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='author',
            name='posted_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='liked_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='posted_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='message',
            name='liked_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='message',
            name='posted_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='movie',
            name='liked_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='movie',
            name='posted_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='music',
            name='liked_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='music',
            name='posted_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='news',
            name='liked_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='news',
            name='posted_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='thing',
            name='liked_by',
            field=models.CharField(default='None', max_length=1000),
        ),
        migrations.AddField(
            model_name='thing',
            name='posted_by',
            field=models.CharField(default='None', max_length=1000),
        ),
    ]
