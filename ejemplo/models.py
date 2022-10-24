from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_de_nacimiento = models.DateField()
    numero_pasaporte = models.IntegerField()
    
def __str__(self):
    return f"{self.nombre}, {self.apellido}, {self.direccion}, {self.email}, {self.fecha_de_nacimiento}, {self.numero_pasaporte}, {self.id}"