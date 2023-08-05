# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-26 20:07
from __future__ import unicode_literals

import os

import six
from django.conf import settings
from django.db import migrations


STACKS_DIRECTORY = os.path.join(settings.FILE_STORAGE_DIRECTORY, 'stacks')


def slug_to_id(apps, schema_migration):
    """
    Forwards migration
    """
    Stack = apps.get_model('stacks', 'Stack')

    # Move the stacks/<id>-<slug> directories to just stacks/<id>
    for stack in Stack.objects.all():
        old_path = os.path.join(STACKS_DIRECTORY, '{}-{}'.format(stack.id, stack.slug))
        new_path = os.path.join(STACKS_DIRECTORY, six.text_type(stack.id))

        if os.path.exists(old_path):
            os.rename(old_path, new_path)


def id_to_slug(apps, schema_migration):
    """
    Reverse migration
    """
    Stack = apps.get_model('stacks', 'Stack')

    # Move the stacks/<id> directories to stacks/<id>-<slug>
    for stack in Stack.objects.all():
        old_path = os.path.join(STACKS_DIRECTORY, '{}-{}'.format(stack.id, stack.slug))
        new_path = os.path.join(STACKS_DIRECTORY, six.text_type(stack.id))

        if os.path.exists(new_path):
            os.rename(new_path, old_path)


class Migration(migrations.Migration):

    dependencies = [
        ('stacks', '0007_0_8_0_migrations'),
    ]

    operations = [
        migrations.RunPython(slug_to_id, id_to_slug),
    ]
