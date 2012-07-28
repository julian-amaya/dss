# Create your views here.
from django.core.paginator import Paginator
from django.template.context import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse

from decorators import json_response
from django.core.cache import cache
from sensors.models import ValorSensor, Alerta
from task import SensorSave

def home(request):
    data = {}
    return render_to_response('index.html', data,context_instance=RequestContext(request)) 

@json_response
def data_sensores(request):
    data = {}
    data['alertas'] = [a.to_json_dict() for a in Alerta.objects.filter(ya_visto=False)]
    data['sensores'] = cache.get('info_sensores')
    return data


def call_celery(request):
	SensorSave.delay()
	return HttpResponse("probando celery")

@json_response
def mark_alert(request,id):
    try:
        a = Alerta.objects.get(id=id)
        a.ya_visto = True
        a.save()
        return "OK"
    except:
        return "not OK"
