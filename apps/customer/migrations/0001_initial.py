# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100, null=True, blank=True)),
                ('contact_point_full_name', models.CharField(max_length=100, null=True, blank=True)),
                ('phone', models.CharField(max_length=100, null=True, blank=True)),
                ('cell_phone', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('national_code', models.CharField(max_length=100, null=True, blank=True)),
                ('service_type', models.CharField(blank=True, max_length=100, null=True, choices=[(b'vpc', 'Virtual Private Cloud (VPC)'), (b'vps', 'Virtual Private Server (VPS)'), (b'dc', 'Datacenter')])),
                ('website_url', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
