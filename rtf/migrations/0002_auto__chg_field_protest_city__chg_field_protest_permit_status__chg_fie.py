# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Protest.city'
        db.alter_column(u'rtf_protest', 'city', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Protest.permit_status'
        db.alter_column(u'rtf_protest', 'permit_status', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Protest.state'
        db.alter_column(u'rtf_protest', 'state', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Protest.location'
        db.alter_column(u'rtf_protest', 'location', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Protest.time'
        db.alter_column(u'rtf_protest', 'time', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Protest.organizer'
        db.alter_column(u'rtf_protest', 'organizer', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Protest.city'
        db.alter_column(u'rtf_protest', 'city', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Protest.permit_status'
        db.alter_column(u'rtf_protest', 'permit_status', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Protest.state'
        db.alter_column(u'rtf_protest', 'state', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Protest.location'
        db.alter_column(u'rtf_protest', 'location', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Protest.time'
        db.alter_column(u'rtf_protest', 'time', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Protest.organizer'
        db.alter_column(u'rtf_protest', 'organizer', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'rtf.protest': {
            'Meta': {'object_name': 'Protest'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_info_status': ('django.db.models.fields.CharField', [], {'default': "'Unrequested'", 'max_length': '50'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'fb_page': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'other': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'permit_status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'reddit_page': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['rtf']