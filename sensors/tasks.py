from celery import task
import requests
import datetime

from sensors.models import ValorSensor
from django.core.cache import cache


def revisar_si_alerta(tipo):
	tipo_problema = tipo
	anterior = cache.get(i)
	obj= {}
	if anterior:
		if anterior['tipo_problema'] == tipo_problema:
			if (fecha - anterior['fecha_hora']).seconds ==30:
				pass 
				#TODO: generar alerta
		else:
			obj ={'fecha_hora':fecha,'valor':s,'tipo_problema':tipo_problema }
			cache.set(i,obj)
	else:
		obj ={'fecha_hora':fecha,'valor':s,'tipo_problema':tipo_problema }
		cache.set(i,obj)

@task
def SensorSave():
	print 'lolo'
	res = requests.get('http://deathstartsensor.herokuapp.com/?star=django')
	a = res.content
	cache.set('info_sensores',a)
	b = a.split(',')
	fecha = b[0]
	sensores = b[1:]
	#print sensores
	fecha = fecha[:-6]
	#print fecha
	fecha = datetime.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")
	for i, s in enumerate(sensores):
		#llaves del tipo {'fecha_hora', 'valor',  tipo_problema, contador }
		if s>100: 
			revisar_si_alerta(2)
		if s<=0:
			revisar_si_alerta(1)
		else:
			pass




