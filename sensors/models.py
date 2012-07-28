from django.db import models

# Create your models here.

class ValorSensor(models.Model):
	PROBLEMA = (
    	(0,'Alerta Interna'),
    	(1, 'Alerta Global'),
    	(2, 'Defectuoso'),
    )
	fecha_hora = models.DateTimeField()
	valor = models.IntegerField()
	num_sensor = models.IntegerField()
	problema = models.IntegerField(choices=PROBLEMA)
	fecha_problema = models.DateTimeField(null=True,blank=True)

class Alerta(models.Model):
	valor = models.IntegerField()
	fecha_hora = models.DateTimeField()
	num_sensor = models.IntegerField()
