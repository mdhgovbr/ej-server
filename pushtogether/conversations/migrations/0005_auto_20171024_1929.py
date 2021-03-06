# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import pushtogether.conversations.validators


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0004_auto_20171013_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='background_color',
            field=models.CharField(blank=True, max_length=7, null=True, validators=[pushtogether.conversations.validators.validate_color]),
        ),
        migrations.AddField(
            model_name='conversation',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='conversations/images/backgrouds'),
        ),
        migrations.AddField(
            model_name='conversation',
            name='dialog',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='conversation',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.IntegerField(choices=[(1, 'AGREE'), (0, 'PASS'), (-1, 'DISAGREE')]),
        ),
    ]
