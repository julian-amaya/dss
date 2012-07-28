# -*- coding: utf-8 -*-
# Create your views here.
from django.core.paginator import Paginator
from django.template.context import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect

from decorators import json_response
from django.core.cache import cache
from sensors.models import ValorSensor, Alerta

def home(request):
    """
    Devuelve la vista que se muestra en la pagina principal. Acción sobre el archivo HTML (index.html)
    """
    data = {}
    return render_to_response('index.html', data,context_instance=RequestContext(request)) 

@json_response
def data_sensores(request):
    """
    Envia por json, la información contenida en la cache, variable data (django.core.cache).
    La variable 'data' consta de las alertas de sensores y además consigue de la cache, 
    'info_sensores', la cual es un cadena(string) con la lectura que se hace al servidor de prueba.
    """
    data = {}
    data['alertas'] = [a.to_json_dict() for a in Alerta.objects.filter(ya_visto=False)]
    sensor_d = cache.get('info_sensores')
    data['sensores'] = cache.get('info_sensores')
    return data

def call_celery(request):
	SensorSave()#.delay()
	return HttpResponse("probando celery")

@json_response
def mark_alert(request,id):
    """
    Este método sirve para actualizar en las vistas, los sensores que ya se han visto, es decir, 
    que ya se ha mostrado una alerta de su estado. 
    """
    try:
        a = Alerta.objects.get(id=id)
        a.ya_visto = True
        a.save()
        return "OK"
    except:
        return "not OK"
