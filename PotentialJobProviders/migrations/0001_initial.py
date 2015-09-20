# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PotentialJobProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('potential_job_provider', models.CharField(max_length=200)),
                ('potential_job_provider_address', models.CharField(max_length=200)),
                ('potential_job_provider_contact_name', models.CharField(max_length=200)),
                ('potential_job_provider_contact_phone', models.CharField(max_length=200)),
                ('potential_job_provider_contact_email', models.EmailField(max_length=254)),
                ('potential_job_provider_notes', models.CharField(max_length=1000)),
            ],
        ),
    ]
