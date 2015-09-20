# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PotentialJobProviders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentialjobprovider',
            name='potential_job_provider_contact_email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='potentialjobprovider',
            name='potential_job_provider_notes',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
