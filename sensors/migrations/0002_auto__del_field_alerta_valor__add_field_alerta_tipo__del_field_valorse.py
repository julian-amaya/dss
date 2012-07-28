# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Alerta.valor'
        db.delete_column('sensors_alerta', 'valor')

        # Adding field 'Alerta.tipo'
        db.add_column('sensors_alerta', 'tipo',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Deleting field 'ValorSensor.fecha_problema'
        db.delete_column('sensors_valorsensor', 'fecha_problema')

        # Adding field 'ValorSensor.contador'
        db.add_column('sensors_valorsensor', 'contador',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Alerta.valor'
        raise RuntimeError("Cannot reverse this migration. 'Alerta.valor' and its values cannot be restored.")
        # Deleting field 'Alerta.tipo'
        db.delete_column('sensors_alerta', 'tipo')

        # Adding field 'ValorSensor.fecha_problema'
        db.add_column('sensors_valorsensor', 'fecha_problema',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ValorSensor.contador'
        db.delete_column('sensors_valorsensor', 'contador')


    models = {
        'sensors.alerta': {
            'Meta': {'object_name': 'Alerta'},
            'fecha_hora': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_sensor': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
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