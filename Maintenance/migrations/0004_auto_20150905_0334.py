# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maintenance', '0003_maintenanceitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancecategory',
            name='category_discontinued',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='maintenancecategory',
            name='category_initiation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='maintenancecategory',
            name='category_last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='maintenanceitem',
            name='item_initiation',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='maintenanceitem',
            name='item_last_serviced',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='maintenanceitem',
            name='item_service_intervals',
            field=models.IntegerField(verbose_name=b'Service Intervals'),
        ),
        migrations.AlterField(
            model_name='maintenanceitem',
            name='removed_from_service',
            field=models.BooleanField(),
        ),
    ]
