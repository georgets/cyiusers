# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'userdb_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cpu_allocation', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'userdb', ['Project'])

        # Adding model 'User'
        db.create_table(u'userdb_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userdb.Project'])),
        ))
        db.send_create_signal(u'userdb', ['User'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'userdb_project')

        # Deleting model 'User'
        db.delete_table(u'userdb_user')


    models = {
        u'userdb.project': {
            'Meta': {'object_name': 'Project'},
            'cpu_allocation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'userdb.user': {
            'Meta': {'object_name': 'User'},
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userdb.Project']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['userdb']