# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.core import serializers
from django.core.paginator import Paginator, InvalidPage
from django.utils import simplejson
from django.http import HttpResponseNotAllowed,\
    HttpResponseForbidden, HttpResponse, Http404, HttpResponseBadRequest

SIZE = getattr(settings, "OBJECTS_PAGE", 20)
DEBUG = getattr(settings, "DEBUG")
MAX_SIZE = getattr(settings, "MAX_OBJECTS_PAGE", 40)

def requires_post(func):
    """
    Retorna un error 405 si el request.method no es POST
    """
    def decorator(request, *args, **kwargs):
        if DEBUG or request.method == 'POST':
            return func(request, *args, **kwargs)
        return HttpResponseNotAllowed(['POST'])
    return decorator

def requires_login(func):
    """
    Retorna un error 403 si el usuario no esta logueado
    """
    def decorator(request, *args, **kwargs):
        if request.user.is_authenticated():
            return func(request, *args, **kwargs)
        return HttpResponseForbidden()
    return decorator


def json_response(func):
    """
    Convierte la respuesta de la funcion en json usando
    la libreria simplejson.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects,HttpResponse):
            return objects 
        try:
            data = simplejson.dumps(objects)
            if 'callback' in request.GET:
                data = '%s(%s);' % (request.GET['callback'],data)
        except:
            data = simplejson.dumps(str(objects))
        if 'callback' in request.GET or 'callback' in request.POST:
            #jsonp
            return HttpResponse(data, "text/javascript")
        else:
            #json
            return HttpResponse(data, "application/json")
    return decorator
