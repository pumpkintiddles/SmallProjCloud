# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_provider', models.CharField(max_length=200)),
                ('job_provider_address', models.CharField(max_length=200)),
                ('job_provider_contact_name', models.CharField(max_length=200)),
                ('job_provider_contact_phone', models.CharField(max_length=200)),
                ('job_provider_contact_email', models.EmailField(max_length=254)),
                ('job_provider_start_date', models.DateTimeField()),
                ('job_provider_rating', models.IntegerField(verbose_name=b'Client rating')),
                ('job_provider_project_totals', models.IntegerField(verbose_name=b'Client total sales/business')),
                ('job_provider_notes', models.CharField(max_length=1000)),
                ('job_provider_conflicts_and_resolution', models.CharField(max_length=2000)),
            ],
        ),
    ]
