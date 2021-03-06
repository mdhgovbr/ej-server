# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 00:50
from __future__ import unicode_literals

from django.db import migrations, models
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
# from ..models import Conversation

def migrate_data_forward(apps, schema_editor):
    Conversation = apps.get_model('conversations', 'Conversation')
    for instance in Conversation.objects.all():
        print("Generating slug for %s" % instance)
        instance.save()

def migrate_data_backward(apps, schema_editor):
    pass

def custom_slugify(value):
    return default_slugify(value).lower()

class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0014_auto_20171117_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='slug',
            preserve_default=False,
            field=AutoSlugField(null=True, default=None, editable=False, populate_from='title', unique=True, slugify=custom_slugify),
        ),
        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backward,
        ),
    ]
