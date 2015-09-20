# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Category_name', models.CharField(max_length=100)),
                ('Category_count', models.IntegerField(verbose_name=b'Membership total')),
                ('Category_initiation', models.DateTimeField()),
                ('Category_last_updated', models.DateTimeField()),
                ('Category_discontinued', models.DateTimeField()),
            ],
        ),
    ]
