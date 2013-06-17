# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Protest'
        db.create_table(u'rtf_protest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('contact_info_status', self.gf('django.db.models.fields.CharField')(default='Unrequested', max_length=50)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('organizer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('permit_status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('reddit_page', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fb_page', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('other', self.gf('django.db.models.fields.TextField')(max_length=2000)),
        ))
        db.send_create_signal(u'rtf', ['Protest'])


    def backwards(self, orm):
        # Deleting model 'Protest'
        db.delete_table(u'rtf_protest')


    models = {
        u'rtf.protest': {
            'Meta': {'object_name': 'Protest'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_info_status': ('django.db.models.fields.CharField', [], {'default': "'Unrequested'", 'max_length': '50'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'fb_page': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'organizer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
            'permit_status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reddit_page': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['rtf']