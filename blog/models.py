from django.db import models
from traitlets import default

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=20)
    construido_por = models.CharField(max_length=30)
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=70, default='')
