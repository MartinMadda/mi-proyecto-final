from django.contrib import admin
from blog.models import Configuracion
from ejemplo.models import Familiar, Empresa

admin.site.register(Familiar)
admin.site.register(Empresa)

admin.site.register(Configuracion)
# usuario admin = root -  password = 1234