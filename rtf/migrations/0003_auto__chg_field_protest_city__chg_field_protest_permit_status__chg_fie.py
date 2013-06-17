# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Protest.city'
        db.alter_column(u'rtf_protest', 'city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Protest.permit_status'
        db.alter_column(u'rtf_protest', 'permit_status', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Protest.twitter'
        db.alter_column(u'rtf_protest', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Protest.fb_page'
        db.alter_column(u'rtf_protest', 'fb_page', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Protest.state'
        db.alter_column(u'rtf_protest', 'state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Protest.other'
        db.alter_column(u'rtf_protest', 'other', self.gf('django.db.models.fields.TextField')(max_length=2000, null=True))

        # Changing field 'Protest.location'
        db.alter_column(u'rtf_protest', 'location', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Protest.time'
        db.alter_column(u'rtf_protest', 'time', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Protest.organizer'
        db.alter_column(u'rtf_protest', 'organizer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Protest.reddit_page'
        db.alter_column(u'rtf_protest', 'reddit_page', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Protest.city'
        db.alter_column(u'rtf_protest', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Protest.permit_status'
        db.alter_column(u'rtf_protest', 'permit_status', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Protest.twitter'
        db.alter_column(u'rtf_protest', 'twitter', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Protest.fb_page'
        db.alter_column(u'rtf_protest', 'fb_page', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Protest.state'
        db.alter_column(u'rtf_protest', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Protest.other'
        db.alter_column(u'rtf_protest', 'other', self.gf('django.db.models.fields.TextField')(default='', max_length=2000))

        # Changing field 'Protest.location'
        db.alter_column(u'rtf_protest', 'location', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Protest.time'
        db.alter_column(u'rtf_protest', 'time', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Protest.organizer'
        db.alter_column(u'rtf_protest', 'organizer', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Protest.reddit_page'
        db.alter_column(u'rtf_protest', 'reddit_page', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    models = {
        u'rtf.protest': {
            'Meta': {'object_name': 'Protest'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_info_status': ('django.db.models.fields.CharField', [], {'default': "'Unrequested'", 'max_length': '50'}),
            'date': ('django.db.models.fields.DateField', [], {}),
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