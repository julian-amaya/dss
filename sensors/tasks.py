from celery import task
import requests
import datetime

from sensors.models import Alerta
from django.core.cache import cache


def revisar_si_alerta(alerta_interna,alerta_publica,i,s, fecha):
    '''
    resiva si la lectura de sensores actual va a generar alertas para
    mostrar en el front end.

    alerta_interna:codigo interno de la alerta de cada sensor
    alerta_publica: codigo publico luego de una acumulacion de alertas internas.
    i: codigo del sensor
    s: valor del sensor
    fecha: fecha de la alerta actual
    '''

    tipo_problema = alerta_interna
    anterior = cache.get(i)
    obj = {}
    if anterior:
        if anterior['tipo_problema'] == tipo_problema:
            if (fecha - anterior['fecha_hora']).seconds ==30:
                Alerta.objects.create(tipo=alerta_publica,fecha_hora=anterior['fecha_hora'],num_sensor=i)
        else:
            obj ={'fecha_hora':fecha,'valor':s,'tipo_problema':tipo_problema }
            cache.set(i,obj)
    else:
        obj = {'fecha_hora':fecha,'valor':s,'tipo_problema':tipo_problema }
        cache.set(i,obj)

def obtener_datos():    
    return requests.get('http://deathstartsensor.herokuapp.com/?star=django')


@task
def SensorSave():
    '''
    Funcion que correra cada segundo solicitando datos al servidor deathstart
    luego revisa el estado de cada uno de los sensores.
    
    '''
    res = obtener_datos()
    a = res.content
    b = a.split(',')
    fecha = b[0]
    sensores = b[1:]
    #print sensores
    fecha = fecha[:-6]
    #print fecha
    fecha = datetime.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")
    temp_con = fecha.strftime('%I:%M:%S %p') + ',' + ','.join(sensores)
    cache.set('info_sensores', temp_con)
    for i, s in enumerate(sensores):
        #llaves del tipo {'fecha_hora', 'valor',  tipo_problema, contador }
        if s>100: 
            alerta_interna = 2
            alerta_publica = 3
            revisar_si_alerta(alerta_interna,alerta_publica,i,s, fecha)
        if s<=0:
            alerta_interna = 1
            alerta_publica = 4
            revisar_si_alerta(alerta_interna,alerta_publica,i,s, fecha)
        else:
            cache.delete(i)
    SensorSave.apply_async()




