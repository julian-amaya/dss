# Create your views here.
from django.core.paginator import Paginator
from django.template.context import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect

from sensors.models import ValorSensor

def home(request):
    data = {}

    valores = ValorSensor.objects.all()
    p = Paginator(valores, 2)

    data['paginator'] = p
    return render_to_response('index.html', data,context_instance=RequestContext(request)) 
