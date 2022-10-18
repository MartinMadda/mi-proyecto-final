from ejemplo.models import Familiar

Familiar(nombre = "Rosario", apellido = "Garcia", direccion ="Rio Parana 745", email = "rogarcia@gmail.com", fechaNac = "1920-12-5", numero_pasaporte = 123123).save()
Familiar(nombre="Romina", apellido= "Londo", direccion="Melo 3790", email= "londoromi@gmail.com", fechaNac = "1930-7-15", numero_pasaporte=454545).save()
Familiar(nombre="Carlos", apellido= "Mario", direccion="Venezuela 840", email= "Carlos_Mario@gmail.com", fechaNac = "1940-9-20", numero_pasaporte=123123).save()


print("Se cargo con éxito los usuarios de pruebas")