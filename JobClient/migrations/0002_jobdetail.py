# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobClient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_name', models.CharField(max_length=100)),
                ('job_identifier', models.CharField(max_length=100)),
                ('job_refered_by', models.CharField(max_length=100)),
                ('job_contact', models.CharField(max_length=100)),
                ('job_contact_phone', models.IntegerField(verbose_name=b'Phone')),
                ('job_initiation_date', models.DateTimeField()),
                ('job_sales_person', models.CharField(max_length=100)),
                ('job_projected_start_install_date', models.DateTimeField()),
                ('job_projected_finish_install_date', models.DateTimeField()),
                ('job_initial_deposit_date', models.DateTimeField()),
                ('job_final_drawings_date', models.DateTimeField()),
                ('job_OE_date', models.DateTimeField()),
                ('job_final_install_date', models.DateTimeField()),
                ('job_closed_out_date', models.DateTimeField()),
                ('job_unusual_issues_or_problems', models.CharField(max_length=1000)),
                ('job_print', models.FileField(upload_to=b'')),
                ('job_provider', models.ForeignKey(to='JobClient.JobClient')),
            ],
        ),
    ]
