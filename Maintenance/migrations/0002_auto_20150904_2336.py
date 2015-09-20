# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maintenance', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Maintenance_category',
            new_name='MaintenanceCategory',
        ),
        migrations.RenameField(
            model_name='maintenancecategory',
            old_name='Category_count',
            new_name='category_count',
        ),
        migrations.RenameField(
            model_name='maintenancecategory',
            old_name='Category_discontinued',
            new_name='category_discontinued',
        ),
        migrations.RenameField(
            model_name='maintenancecategory',
            old_name='Category_initiation',
            new_name='category_initiation',
        ),
        migrations.RenameField(
            model_name='maintenancecategory',
            old_name='Category_last_updated',
            new_name='category_last_updated',
        ),
        migrations.RenameField(
            model_name='maintenancecategory',
            old_name='Category_name',
            new_name='category_name',
        ),
    ]
