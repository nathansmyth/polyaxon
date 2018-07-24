# Generated by Django 2.0.3 on 2018-07-24 20:15

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import libs.blacklist
import re


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_bookmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='experimentjob',
            name='affinity',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experimentjob',
            name='node_selector',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='experimentjob',
            name='tolerations',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid'), libs.blacklist.validate_blacklist_name]),
        ),
    ]
