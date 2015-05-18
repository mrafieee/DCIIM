# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Port'
        db.create_table(u'datacenter_port', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('router', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Router'])),
            ('network', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Network'])),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datacenter', ['Port'])

        # Adding model 'Instance'
        db.create_table(u'datacenter_instance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Project'])),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Infrastructure'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ram', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('hdd', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cpu', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('flavor', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('hypervisor', self.gf('django.db.models.fields.CharField')(default='qemu', max_length=100)),
            ('gateway', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Router'])),
            ('network', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Network'])),
            ('openstack_internal_ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('internal_ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('external_ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('datacenter_firewall', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('internal_firewall', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'datacenter', ['Instance'])

        # Adding field 'Infrastructure.rackno'
        db.add_column(u'datacenter_infrastructure', 'rackno',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)

        # Adding field 'Network.type'
        db.add_column(u'datacenter_network', 'type',
                      self.gf('django.db.models.fields.CharField')(default='local', max_length=100),
                      keep_default=False)

        # Adding field 'Network.gateway'
        db.add_column(u'datacenter_network', 'gateway',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)

        # Adding field 'Network.dhcp'
        db.add_column(u'datacenter_network', 'dhcp',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Project.resources'
        db.add_column(u'datacenter_project', 'resources',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Router.internal_ip'
        db.add_column(u'datacenter_router', 'internal_ip',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)

        # Adding field 'Router.external_ip'
        db.add_column(u'datacenter_router', 'external_ip',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Port'
        db.delete_table(u'datacenter_port')

        # Deleting model 'Instance'
        db.delete_table(u'datacenter_instance')

        # Deleting field 'Infrastructure.rackno'
        db.delete_column(u'datacenter_infrastructure', 'rackno')

        # Deleting field 'Network.type'
        db.delete_column(u'datacenter_network', 'type')

        # Deleting field 'Network.gateway'
        db.delete_column(u'datacenter_network', 'gateway')

        # Deleting field 'Network.dhcp'
        db.delete_column(u'datacenter_network', 'dhcp')

        # Deleting field 'Project.resources'
        db.delete_column(u'datacenter_project', 'resources')

        # Deleting field 'Router.internal_ip'
        db.delete_column(u'datacenter_router', 'internal_ip')

        # Deleting field 'Router.external_ip'
        db.delete_column(u'datacenter_router', 'external_ip')


    models = {
        u'datacenter.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secondary_email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'datacenter.infrastructure': {
            'Meta': {'object_name': 'Infrastructure'},
            'cpu': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'data_center_code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'guarantee': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'hdd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hdd_raid': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nic_count': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rackno': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ram': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.InfrastructureRole']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.InfrastructureType']"})
        },
        u'datacenter.infrastructurerole': {
            'Meta': {'object_name': 'InfrastructureRole'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'datacenter.infrastructuretype': {
            'Meta': {'object_name': 'InfrastructureType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'datacenter.instance': {
            'Meta': {'object_name': 'Instance'},
            'cpu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'datacenter_firewall': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'external_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'flavor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gateway': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Router']"}),
            'hdd': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hypervisor': ('django.db.models.fields.CharField', [], {'default': "'qemu'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_firewall': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'internal_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Infrastructure']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Network']"}),
            'openstack_internal_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Project']"}),
            'ram': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'datacenter.network': {
            'Meta': {'object_name': 'Network'},
            'dhcp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'gateway': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'netmask': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Project']"}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'local'", 'max_length': '100'})
        },
        u'datacenter.nic': {
            'Meta': {'object_name': 'Nic'},
            'external_ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'firewall_access_rules': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infrastructure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Infrastructure']"}),
            'internal_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'switch_port': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'vlan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'datacenter.port': {
            'Meta': {'object_name': 'Port'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Network']"}),
            'router': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Router']"})
        },
        u'datacenter.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Customer']"}),
            'resources': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 14, 0, 0)'}),
            'stop_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'datacenter.router': {
            'Meta': {'object_name': 'Router'},
            'external_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Project']"})
        },
        u'datacenter.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Project']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['datacenter']