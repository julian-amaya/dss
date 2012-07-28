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
    fecha_hora = models.DateTimeField()
    valor = models.IntegerField()
    num_sensor = models.IntegerField()
    problema = models.IntegerField(choices=PROBLEMA)
    #fecha_problema = models.DateTimeField(null=True,blank=True)
    contador = models.IntegerField(null=True,blank=True)

    def save(self, *args, **kwargs):

        # try:
        #     vs = ValorSensor.objects.order_by('-fecha_hora')[0]
        #     if vs.fecha_problema:
        #         # si hay problema, reviso si yo sigo en problema y si ha pasado suficiente tiempo 
        #         # y creo alerta
        #         if (self.fecha_hora - vs.fecha_hora).seconds > 2:
        #             # sensor defectuoso
        #             self.problema = 2
        #         if valor <100:
        #             #en este caso no hay problemas
        #             self.fecha_problema = None
        #         elif valor == 0:
        #             #en este caso hay problema
        # except:
        #     pass
        super(ValorSensor, self).save(*args, **kwargs)




class Alerta(models.Model):
    tipo = models.IntegerField()
    fecha_hora = models.DateTimeField()
    num_sensor = models.IntegerField()

    def to_json_dict(self):
        return {'tipo':self.tipo,'fecha_hora':self.fecha_hora,'num_sensor':self.numsensor}
