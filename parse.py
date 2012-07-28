#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
os.environ['DJANGO_SETTINGS_MODULE']='dss.settings'
from django.core.management import execute_manager
#from django.db import transaction

import imp
try:
        imp.find_module('dss.settings') # Assumed to be in the same directory.
except ImportError:
        import sys
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
        sys.exit(1)
		
import requests
import datetime
from sensors.models import ValorSensor
res = requests.get('http://deathstartsensor.herokuapp.com/?star=django')
a=res.content
#[fecha,sensor]
b=a.split(',')
fecha=b[0]
sensores=b[1:]
print sensores
fecha = fecha[:-6]
print fecha
print datetime.datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S")


for i,s in enumerate(sensores):
	print i,s
	ValorSensor.objects.create(fecha_hora=fecha,valor=s) 
	
	