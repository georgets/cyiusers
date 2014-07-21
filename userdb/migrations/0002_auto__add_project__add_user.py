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
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('cpu_allocation', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('linklings_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('pi_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('pi', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_pi', null=True, to=orm['userdb.User'])),
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
            'linklings_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pi': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_pi'", 'null': 'True', 'to': u"orm['userdb.User']"}),
            'pi_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
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