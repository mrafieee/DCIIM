# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='service_type',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'vpc', 'Virtual Private Cloud (VPC)'), (b'vps', 'Virtual Private Server (VPS)'), (b'dc', 'Datacenter'), (b'saas', 'SaaS')]),
        ),
    ]
