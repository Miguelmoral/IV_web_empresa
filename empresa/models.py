from django.db import models

class Datos(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    persona = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    puntuacion = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre_empresa
