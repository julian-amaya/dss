# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ValorSensor'
        db.create_table('sensors_valorsensor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_hora', self.gf('django.db.models.fields.DateTimeField')()),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('num_sensor', self.gf('django.db.models.fields.IntegerField')()),
            ('problema', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_problema', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('sensors', ['ValorSensor'])

        # Adding model 'Alerta'
        db.create_table('sensors_alerta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_hora', self.gf('django.db.models.fields.DateTimeField')()),
            ('num_sensor', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('sensors', ['Alerta'])


    def backwards(self, orm):
        # Deleting model 'ValorSensor'
        db.delete_table('sensors_valorsensor')

        # Deleting model 'Alerta'
        db.delete_table('sensors_alerta')


    models = {
        'sensors.alerta': {
            'Meta': {'object_name': 'Alerta'},
            'fecha_hora': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_sensor': ('django.db.models.fields.IntegerField', [], {}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        'sensors.valorsensor': {
            'Meta': {'object_name': 'ValorSensor'},
            'fecha_hora': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_problema': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_sensor': ('django.db.models.fields.IntegerField', [], {}),
            'problema': ('django.db.models.fields.IntegerField', [], {}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['sensors']