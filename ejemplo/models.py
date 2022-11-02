from django.db import models

class Familiar(models.Model): #en la terminal ingrese "pip install django_crispy-forms"
    nombre = models.CharField(max_length=100) # en blog/models esta la clase "configuracion"
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_de_nacimiento = models.DateField()
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.direccion}, {self.email}, {self.fecha_de_nacimiento}, {self.numero_pasaporte}, {self.id}"

class Empresa(models.Model):
    nombre_empresa=models.CharField(max_length=100)
    url_empresa=models.CharField(max_length=300)
    telefono=models.IntegerField()

    def __str__(self): #proximamente mostramos con autorizacion login
        return f"{self.nombre_empresa}, {self.url_empresa}, {self.telefono}, {self.id}"

class Mascota(models.Model):
    nombre_mascota=models.CharField(max_length=100)
    animal=models.CharField(max_length=300)
    telefono_dueño=models.IntegerField()

    def __str__(self):
        return f"{self.nombre_mascota},{self.animal},{self.telefono_dueño}"








