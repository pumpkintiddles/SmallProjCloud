# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_rank', models.CharField(max_length=100)),
                ('employee_position', models.CharField(max_length=30)),
                ('employee_start_date', models.DateTimeField()),
                ('employee_suspended_date', models.DateTimeField(null=True, blank=True)),
                ('employee_account_closed_date', models.DateTimeField(null=True, blank=True)),
                ('employee_account_reopened_date', models.DateTimeField(null=True, blank=True)),
                ('employee_vacation_left', models.IntegerField(verbose_name=b'Vacation days left')),
                ('employee_sick_days', models.IntegerField(verbose_name=b'Sick days left')),
                ('employee_late_days', models.IntegerField(verbose_name=b'Late days')),
                ('employee_pay_rate', models.IntegerField(verbose_name=b'Pay rate')),
                ('employee_stats', models.IntegerField(verbose_name=b'Employee stats')),
                ('employee_awards', models.IntegerField(verbose_name=b'Employee awards')),
            ],
        ),
    ]
