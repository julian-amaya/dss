from django.db import models

# Create your models here.

PROBLEMA = (
    (0, 'Normal'),
    (1, 'Alerta Interna defectuoso'),
    (2, 'Alerta Interna ataque'),
    (3, 'Alerta Ataque'),
    (4, 'Alerta Defectuoso'),
)

class ValorSensor(models.Model):
    '''
    Tabla para guardar los valores de sensores - no se esta usando pero 
    se guarda por backcompatibility
    '''
    fecha_hora = models.DateTimeField()
    valor = models.IntegerField()
    num_sensor = models.IntegerField()
    problema = models.IntegerField(choices=PROBLEMA)
    #fecha_problema = models.DateTimeField(null=True,blank=True)
    contador = models.IntegerField(null=True,blank=True)



# 3, 4
ALERTA_CHOICES = (
    # (0, 'Normal'),
    # (1, 'Alerta Interna defectuoso'),
    # (2, 'Alerta Interna ataque'),
    (3, 'Alerta Ataque'),
    (4, 'Alerta Defectuoso'),
)
class Alerta(models.Model):
    '''
    Modelo alerta, guarda todas las alertas publicas generadas.
    '''
    tipo = models.IntegerField(choices=ALERTA_CHOICES)
    fecha_hora = models.DateTimeField()
    num_sensor = models.IntegerField()
    ya_visto = models.BooleanField(default=False)


    def to_json_dict(self):
        '''
        Convierte este modelo a json para que se pueda utilizar mas facil en las vistas
        '''
        return {'id':self.id,'tipo':self.tipo,'fecha_hora':str(self.fecha_hora),'num_sensor':self.num_sensor}
