# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobClient', '0004_auto_20150908_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobclient',
            name='job_provider_notes',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
