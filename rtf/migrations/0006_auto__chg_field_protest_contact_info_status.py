# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Protest.contact_info_status'
        db.alter_column(u'rtf_protest', 'contact_info_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # Changing field 'Protest.contact_info_status'
        db.alter_column(u'rtf_protest', 'contact_info_status', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'rtf.protest': {
            'Meta': {'object_name': 'Protest'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_info_status': ('django.db.models.fields.CharField', [], {'default': "'Unrequested'", 'max_length': '50', 'null': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'fb_page': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'other': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'null': 'True'}),
            'permit_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'reddit_page': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['rtf']