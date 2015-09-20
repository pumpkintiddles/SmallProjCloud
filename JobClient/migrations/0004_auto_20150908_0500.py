# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobClient', '0003_auto_20150908_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobclient',
            name='job_provider_conflicts_and_resolution',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
    ]
