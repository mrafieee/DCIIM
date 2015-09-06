# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0003_auto_20150713_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=100, null=True, blank=True)),
                ('instance_count', models.CharField(max_length=100, null=True, blank=True)),
                ('projects_count', models.CharField(max_length=100, null=True, blank=True)),
                ('floating_ips_count', models.CharField(max_length=100, null=True, blank=True)),
                ('images_count', models.CharField(max_length=100, null=True, blank=True)),
                ('computes_node_count', models.CharField(max_length=100, null=True, blank=True)),
                ('controller_node_count', models.CharField(max_length=100, null=True, blank=True)),
                ('network_node_count', models.CharField(max_length=100, null=True, blank=True)),
                ('network_count', models.CharField(max_length=100, null=True, blank=True)),
                ('routers_count', models.CharField(max_length=100, null=True, blank=True)),
                ('total_vcpu', models.CharField(max_length=100, null=True, blank=True)),
                ('total_memory', models.CharField(max_length=100, null=True, blank=True)),
                ('total_local_disk', models.CharField(max_length=100, null=True, blank=True)),
                ('vcpu_used', models.CharField(max_length=100, null=True, blank=True)),
                ('memory_used', models.CharField(max_length=100, null=True, blank=True)),
                ('local_disk_used', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'History',
            },
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='group',
            field=models.CharField(default=b'OX', max_length=100, choices=[(b'OX', b'OX'), (b'NeX', b'NeX'), (b'DeX', b'DeX'), (b'Kerman', b'Kerman')]),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='hdd_raid',
            field=models.CharField(default=b'raid5', max_length=100, choices=[(b'raid0', b'RAID 0'), (b'raid1', b'RAID 1'), (b'raid5', b'RAID 5'), (b'raid1+0', b'RAID 1 + 0'), (b'softwareraid5', b'Software RAID 5'), (b'raid1+ceph', b'RAID 1 + ceph')]),
        ),
    ]
