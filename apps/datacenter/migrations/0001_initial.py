# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_center_code', models.CharField(max_length=100, null=True, blank=True)),
                ('hostname', models.CharField(max_length=100)),
                ('ram', models.CharField(max_length=100)),
                ('cpu', models.CharField(max_length=100)),
                ('hdd', models.CharField(max_length=100)),
                ('hdd_raid', models.CharField(default=b'raid5', max_length=100, choices=[(b'raid0', b'RAID 0'), (b'raid1', b'RAID 1'), (b'raid5', b'RAID 5'), (b'raid1+0', b'RAID 1 + 0'), (b'softwareraid5', b'Software RAID 5')])),
                ('operating_system', models.CharField(default=b'Debian Wheezy', max_length=100)),
                ('nic_count', models.CharField(max_length=100)),
                ('rack_number', models.CharField(max_length=100)),
                ('rack_u_number', models.CharField(max_length=100)),
                ('guarantee', models.CharField(max_length=300, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='InfrastructureRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Infrastructure Role',
                'verbose_name_plural': 'Infrastructure Roles',
            },
        ),
        migrations.CreateModel(
            name='InfrastructureType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Infrastructure Type',
                'verbose_name_plural': 'Infrastructure Types',
            },
        ),
        migrations.CreateModel(
            name='Nic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='for example eth0, eth1, ...', max_length=100, null=True, blank=True)),
                ('mac', models.CharField(max_length=100)),
                ('vlan', models.CharField(default=b'vlan90', max_length=100, null=True, blank=True, choices=[(b'trunk', b'Trunk'), (b'vlan90', b'Vlan 90'), (b'vlan91', b'Vlan 91'), (b'valn92', b'Vlan 92'), (b'vlan93', b'Vlan 93'), (b'vlan94', b'Vlan 94'), (b'vlan95', b'Vlan 95')])),
                ('switch_port', models.CharField(max_length=100, null=True, blank=True)),
                ('internal_ip', models.CharField(max_length=100)),
                ('external_ip', models.CharField(max_length=100, null=True, blank=True)),
                ('firewall_access_rules', models.CharField(max_length=100)),
                ('infrastructure', models.ForeignKey(to='datacenter.Infrastructure')),
            ],
        ),
        migrations.AddField(
            model_name='infrastructure',
            name='role',
            field=models.ForeignKey(to='datacenter.InfrastructureRole'),
        ),
        migrations.AddField(
            model_name='infrastructure',
            name='type',
            field=models.ForeignKey(to='datacenter.InfrastructureType'),
        ),
    ]
