# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0006_auto_20150901_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Changes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 9, 6, 4, 10, 6, 207944))),
                ('type', models.CharField(max_length=100, choices=[(b'Intallation', b'Intallation'), (b'Openstack upgrade', b'Openstack upgrade'), (b'OS upgrade', b'OS upgrade'), (b'Other', b'Other')])),
                ('description', models.TextField(null=True, blank=True)),
                ('infrastructure', models.ForeignKey(to='datacenter.Infrastructure')),
            ],
        ),
    ]
