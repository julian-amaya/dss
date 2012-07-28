# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, redirect

from sensors.models import ValorSensor

def home(request):
    data = {}

    valores = ValorSensor.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(valores, 2)
    try:
        sensores = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sensores = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sensores = paginator.page(paginator.num_pages)
    data['sensores_paginator'] = paginator
    data['sensores'] = sensores

    return render_to_response('index.html', data,context_instance=RequestContext(request)) 
