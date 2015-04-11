# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'datacenter_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('secondary_email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'datacenter', ['Customer'])

        # Adding model 'Project'
        db.create_table(u'datacenter_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 4, 11, 0, 0))),
            ('stop_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Customer'])),
        ))
        db.send_create_signal(u'datacenter', ['Project'])

        # Adding model 'Infrastructure'
        db.create_table(u'datacenter_infrastructure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_center_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('server_type', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('ram', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cpu', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hdd', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hdd_raid', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('operating_system', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nic_count', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nic_mac', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nic_vlan', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nic_switch_port', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nic_internal_ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nic_external_ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('firewall_access_rules', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('guarantee', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'datacenter', ['Infrastructure'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'datacenter_customer')

        # Deleting model 'Project'
        db.delete_table(u'datacenter_project')

        # Deleting model 'Infrastructure'
        db.delete_table(u'datacenter_infrastructure')


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
            'firewall_access_rules': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'guarantee': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'hdd': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hdd_raid': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nic_count': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nic_external_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nic_internal_ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nic_mac': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nic_switch_port': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nic_vlan': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'operating_system': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ram': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'server_type': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'datacenter.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Customer']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 11, 0, 0)'}),
            'stop_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['datacenter']