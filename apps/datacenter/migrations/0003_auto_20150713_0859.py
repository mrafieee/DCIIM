# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0002_infrastructure_datacenter_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='infrastructure',
            name='group',
            field=models.CharField(default=b'OX', max_length=100, choices=[(b'OX', b'OX'), (b'NeX', b'NeX'), (b'DeX', b'DeX')]),
        ),
        migrations.AddField(
            model_name='infrastructure',
            name='state',
            field=models.CharField(default=b'Operational', max_length=100, choices=[(b'Operational', b'Operational'), (b'Under maintenance', b'Under maintenance'), (b'Damaged', b'Damaged'), (b'Not Configured', b'Not Configured')]),
        ),
    ]
