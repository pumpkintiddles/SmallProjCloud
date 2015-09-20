# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobClient', '0005_auto_20150909_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetail',
            name='job_OE_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='job_closed_out_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='job_final_drawings_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='job_final_install_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='job_initial_deposit_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='job_print',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='job_projected_finish_install_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='job_projected_start_install_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jobdetail',
            name='job_unusual_issues_or_problems',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
