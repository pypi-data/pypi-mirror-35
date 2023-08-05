# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-02 21:22
from __future__ import unicode_literals

import json

import django.core.files.base
from django.db import migrations


def get_global_orchestration_properties(account):
    if not account.global_orch_props_file:
        return {}
    with open(account.global_orch_props_file.path) as f:
        return json.loads(f.read())


def set_global_orchestration_properties(account, props):
    props_json = json.dumps(props, indent=4)
    if not account.global_orch_props_file:
        account.global_orch_props_file.save('global_orch.props', django.core.files.base.ContentFile(props_json))
    else:
        with open(account.global_orch_props_file.path, 'w') as f:
            f.write(props_json)


def props_file_to_db(apps, schema_migration):
    CloudAccount = apps.get_model('cloud', 'CloudAccount')

    for account in CloudAccount.objects.all():
        # Grab the properties from the file and save them to the database
        account.global_orchestration_properties = get_global_orchestration_properties(account)
        account.save()


def db_to_props_file(apps, schema_migration):
    CloudAccount = apps.get_model('cloud', 'CloudAccount')

    for account in CloudAccount.objects.all():
        # Grab the properties from the database and save them to the filesystem
        set_global_orchestration_properties(account, account.global_orchestration_properties)
        account.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0005_0_8_0_migrations'),
    ]

    operations = [
        # Then copy everything from all the props files into the properties field
        migrations.RunPython(props_file_to_db, db_to_props_file),
    ]
