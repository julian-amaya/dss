# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Alerta.ya_visto'
        db.add_column('sensors_alerta', 'ya_visto',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Alerta.ya_visto'
        db.delete_column('sensors_alerta', 'ya_visto')


    models = {
        'sensors.alerta': {
            'Meta': {'object_name': 'Alerta'},
            'fecha_hora': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_sensor': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'ya_visto': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'sensors.valorsensor': {
            'Meta': {'object_name': 'ValorSensor'},
            'contador': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_hora': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_sensor': ('django.db.models.fields.IntegerField', [], {}),
            'problema': ('django.db.models.fields.IntegerField', [], {}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['sensors']