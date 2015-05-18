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
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 4, 13, 0, 0))),
            ('stop_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Customer'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'datacenter', ['Project'])

        # Adding model 'User'
        db.create_table(u'datacenter_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Project'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datacenter', ['User'])

        # Adding model 'Network'
        db.create_table(u'datacenter_network', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('network', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('netmask', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datacenter', ['Network'])

        # Adding model 'Router'
        db.create_table(u'datacenter_router', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datacenter', ['Router'])

        # Adding model 'InfrastructureType'
        db.create_table(u'datacenter_infrastructuretype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'datacenter', ['InfrastructureType'])

        # Adding model 'InfrastructureRole'
        db.create_table(u'datacenter_infrastructurerole', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'datacenter', ['InfrastructureRole'])

        # Adding model 'Infrastructure'
        db.create_table(u'datacenter_infrastructure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_center_code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.InfrastructureRole'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.InfrastructureType'])),
            ('ram', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cpu', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hdd', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hdd_raid', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('operating_system', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nic_count', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('guarantee', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'datacenter', ['Infrastructure'])

        # Adding model 'Nic'
        db.create_table(u'datacenter_nic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('infrastructure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datacenter.Infrastructure'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('vlan', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('switch_port', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('internal_ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('external_ip', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('firewall_access_rules', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datacenter', ['Nic'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'datacenter_customer')

        # Deleting model 'Project'
        db.delete_table(u'datacenter_project')

        # Deleting model 'User'
        db.delete_table(u'datacenter_user')

        # Deleting model 'Network'
        db.delete_table(u'datacenter_network')

        # Deleting model 'Router'
        db.delete_table(u'datacenter_router')

        # Deleting model 'InfrastructureType'
        db.delete_table(u'datacenter_infrastructuretype')

        # Deleting model 'InfrastructureRole'
        db.delete_table(u'datacenter_infrastructurerole')

        # Deleting model 'Infrastructure'
        db.delete_table(u'datacenter_infrastructure')

        # Deleting model 'Nic'
        db.delete_table(u'datacenter_nic')


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
        u'datacenter.network': {
            'Meta': {'object_name': 'Network'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'netmask': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Project']"})
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
        u'datacenter.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datacenter.Customer']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 4, 13, 0, 0)'}),
            'stop_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'datacenter.router': {
            'Meta': {'object_name': 'Router'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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