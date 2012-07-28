from django.db import models

# Create your models here.

class ValorSensor(models.Model):
	PROBLEMA = (
    	(0,'Alerta Interna'),
    	(1, 'Alerta Global'),
    	(2, 'Defectuoso'),
    )
	fecha_hora = DateTimeField()
	valor = IntegerField()
	num_sensor = IntegerField()
	problema = IntegerField(choices=PROBLEMA)
	fecha_problema = DateTimeField(null=True,blank=True)

class Alerta(models.Model):
	valor = IntegerField()
	fecha_hora = DateTimeField()
	num_sensor = IntegerField()
