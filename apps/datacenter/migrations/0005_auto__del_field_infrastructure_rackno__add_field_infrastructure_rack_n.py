# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Infrastructure.rackno'
        db.delete_column(u'datacenter_infrastructure', 'rackno')

        # Adding field 'Infrastructure.rack_number'
        db.add_column(u'datacenter_infrastructure', 'rack_number',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)

        # Adding field 'Infrastructure.rack_u_number'
        db.add_column(u'datacenter_infrastructure', 'rack_u_number',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)


        # Changing field 'Infrastructure.data_center_code'
        db.alter_column(u'datacenter_infrastructure', 'data_center_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):
        # Adding field 'Infrastructure.rackno'
        db.add_column(u'datacenter_infrastructure', 'rackno',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=100),
                      keep_default=False)

        # Deleting field 'Infrastructure.rack_number'
        db.delete_column(u'datacenter_infrastructure', 'rack_number')

        # Deleting field 'Infrastructure.rack_u_number'
        db.delete_column(u'datacenter_infrastructure', 'rack_u_number')


        # Changing field 'Infrastructure.data_center_code'
        db.alter_column(u'datacenter_infrastructure', 'data_center_code', self.gf('django.db.models.fields.CharField')(default=' ', max_length=100))

    models = {
        u'datacenter.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contract_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 27, 0, 0)'}),
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
            'data_center_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'guarantee': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'hdd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hdd_raid': ('django.db.models.fields.CharField', [], {'default': "'raid5'", 'max_length': '100'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nic_count': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'default': "'Debian Wheezy'", 'max_length': '100'}),
            'rack_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rack_u_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'external_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'flavor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gateway': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Router']"}),
            'glance_image': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hdd': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hypervisor': ('django.db.models.fields.CharField', [], {'default': "'qemu'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_firewall': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'vlan': ('django.db.models.fields.CharField', [], {'default': "'vlan90'", 'max_length': '100', 'null': 'True', 'blank': 'True'})
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
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 27, 0, 0)'}),
            'stop_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'datacenter.router': {
            'Meta': {'object_name': 'Router'},
            'external_ip': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
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
            'role': ('django.db.models.fields.CharField', [], {'default': "'member'", 'max_length': '100'})
        }
    }

    complete_apps = ['datacenter']