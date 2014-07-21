# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.scientific_field'
        db.add_column(u'userdb_project', 'scientific_field',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.scientific_field'
        db.delete_column(u'userdb_project', 'scientific_field')


    models = {
        u'userdb.project': {
            'Meta': {'object_name': 'Project'},
            'cpu_allocation': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linklings_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pi': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_pi'", 'null': 'True', 'to': u"orm['userdb.User']"}),
            'pi_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'scientific_field': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
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