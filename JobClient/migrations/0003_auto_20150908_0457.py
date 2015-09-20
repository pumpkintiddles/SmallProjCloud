# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobClient', '0002_jobdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobclient',
            name='job_provider_conflicts_and_resolution',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='jobclient',
            name='job_provider_notes',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
