from django.contrib import admin

from .models import Alerta

class AlertaAdmin(admin.ModelAdmin):
    list_display = ['tipo','fecha_hora', 'num_sensor', 'ya_visto']

admin.site.register(Alerta, AlertaAdmin)