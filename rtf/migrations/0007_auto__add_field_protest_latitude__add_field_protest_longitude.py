# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Protest.latitude'
        db.add_column(u'rtf_protest', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Protest.longitude'
        db.add_column(u'rtf_protest', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Protest.latitude'
        db.delete_column(u'rtf_protest', 'latitude')

        # Deleting field 'Protest.longitude'
        db.delete_column(u'rtf_protest', 'longitude')


    models = {
        u'rtf.protest': {
            'Meta': {'object_name': 'Protest'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_info_status': ('django.db.models.fields.CharField', [], {'default': "'Unrequested'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'fb_page': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'permit_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'reddit_page': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rtf']