import requests
import datetime
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