# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maintenance', '0002_auto_20150904_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=100)),
                ('item_id', models.IntegerField(verbose_name=b'Membership total')),
                ('item_initiation', models.DateTimeField()),
                ('item_last_serviced', models.DateTimeField()),
                ('item_service_intervals', models.DateTimeField()),
                ('removed_from_service', models.DateTimeField()),
                ('category_name_reference', models.ForeignKey(to='Maintenance.MaintenanceCategory')),
            ],
        ),
    ]
