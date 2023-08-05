# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-14 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import stackdio.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('sls_path', models.CharField(max_length=128, verbose_name='SLS Path')),
                ('host', models.CharField(max_length=256, verbose_name='Host')),
                ('status', models.CharField(choices=[('cancelled', 'cancelled'), ('failed', 'failed'), ('succeeded', 'succeeded')], default='queued', max_length=32, verbose_name='Status')),
                ('health', models.CharField(choices=[('healthy', 'healthy'), ('unhealthy', 'unhealthy')], default='unknown', max_length=32, verbose_name='Health')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('activity', models.CharField(blank=True, choices=[('unknown', 'unknown'), ('queued', 'queued'), ('launching', 'launching'), ('provisioning', 'provisioning'), ('orchestrating', 'orchestrating'), ('', ''), ('pausing', 'pausing'), ('paused', 'paused'), ('resuming', 'resuming'), ('terminating', 'terminating'), ('terminated', 'terminated'), ('executing', 'executing'), ('dead', 'dead')], default='', max_length=32, verbose_name='Activity')),
                ('create_users', models.BooleanField(verbose_name='Create SSH Users')),
                ('properties', stackdio.core.fields.JSONField(verbose_name='Properties')),
                ('orchestrate_sls_path', models.CharField(default='orchestrate', max_length=255, verbose_name='Orchestrate SLS Path')),
            ],
            options={
                'ordering': ('name',),
                'default_permissions': ('delete', 'admin', 'create', 'update', 'ssh', 'orchestrate', 'provision', 'view'),
            },
        ),
        migrations.AddField(
            model_name='componentmetadata',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='component_metadatas', to='environments.Environment'),
        ),
    ]
