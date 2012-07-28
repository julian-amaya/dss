from celery import task
import requests
import datetime

from sensors.models import ValorSensor


@task
def SensorSave():
    res = requests.get('http://deathstartsensor.herokuapp.com/?star=django')
    a = res.content
    b = a.split(',')
    fecha = b[0]
    sensores = b[1:]
    #print sensores
    fecha = fecha[:-6]
    #print fecha
    fecha = datetime.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")
    for i, s in enumerate(sensores):
        ValorSensor.objects.create(fecha_hora=fecha, valor=s)
