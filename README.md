# Proyecto MVT Django por Martín Maddalena y Johan Nahuel Romero

## Instalaciones desde VSCode
### Instalar Python

```bash
$ pip install python
```
### Instalar Django
```bash
$ pip install django
```
### Instalar Crispy-forms
```bash
$ pip install django_crispy-forms
```

## Verificar que este todo correctamente instalado

- Python en el bash
```bash
$ python --version
Python 3.10.7
```
- Django en el shell
```ps
>>> import django
>>> django.VERSION
(4, 1, 2, 'final', 0)
>>>
```

# Iniciamos nuestro proyecto Django

-Antes de comenzar recordemos que debemos iniciar ```git init .``` (no olvidar el espacio y punto) en el terminal, ubicado dentro de nuestra carpeta raiz.

### Lo primero que debemos hacer es crear nuestro repositorio en github y copiar la url.

- ```git clone <reemplazar_con_tu_repo_url> .```**No olvidar el espacio y el punto**

"En nuestro caso creamos 2 app **ejemplo** y **blog**, vamos a llamar al proyecto: **proyecto_coderhouse**

Una vez clonado, en el bash iniciamos nuestro proyecto y app.

- ```django-admin startproject proyecto_coderhouse .```
**No olvidar el espacio y el punto**

- ```python manage.py startapp ejemplo```
- ```python manage.py startapp blog```

- ```python manage.py migrate```

- Crear la siguiente estructura de carpetas:
  ```ejemplo/templates/ejemplo```
- y lo mismo con blog:
  ```blog/templates/blog```

- Realizamos el ```python manage.py makemigrations```
 esto nos sirve para generar el archivo 0001_initial.py que se encarga de gestionar la db.

- Crear la siguiente estructura de carpetas:
  ```blog/static/blog```

- Desde el siguiente link < [https://startbootstrap.com/previews/blog-home](https://startbootstrap.com/previews/blog-home) > descargar las carpetas ```assets, css y js```, las cuales vamos a copiar dentro de ```blog/static/blog```

- Dentro de ```blog/templates/blog``` creamos un archivo  HTML en nuestro caso ```index.html``` y copiamos lo siguiente

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title> 
     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script> 
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.min.js" integrity="sha384-IDwe1+LCz02ROU9k972gdyvl+AESN10+x7tBKgc9I5HFtuNz0wWnPclzo6p9vxnk" crossorigin="anonymous"></script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
          <a class="navbar-brand" href="    {% url 'Inicio' %}  ">Pagina Inicial</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">

            <ul class="navbar-nav me-auto mb-2 mb-lg-0">

                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'Alta' %} ">Cargar Familiar</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'Buscar' %}">Buscar Familiar</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'Lista' %}">Ver Familiar</a>
                </li>

            </ul>
          </div>
        </div>
      </nav>

      <div class="container">
        
            <center><svg width="1000" height="150"><rect width="150" height="150" fill="orange">
            <animate attributeName="x" from="0" to="500" dur="10s" fill="freeze" repeatCount="200"/></rect></svg>
            <h1>Proyecto Martin y Johan</h1></center>
            <div class="row">
                <!-- Blog entries-->
                <div class="col-lg-8">
                    <!-- Featured blog post-->
                    <div class="card mb-4">
                        <a href="#!"><img class="card-img-top" src="https://dummyimage.com/850x350/dee2e6/6c757d.jpg" alt="..." /></a>
                        <div class="card-body">
                            <div class="small text-muted">January 1, 2022</div>
                            <h2 class="card-title">Featured Post Title</h2>
                            <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla? Quos cum ex quis soluta, a laboriosam. Dicta expedita corporis animi vero voluptate voluptatibus possimus, veniam magni quis!</p>
                            <a class="btn btn-primary" href="#!">Read more →</a>
                        </div>
                    </div>
                    <!-- Nested row for non-featured blog posts-->
                    <div class="row">
                        <div class="col-lg-6">
                            <!-- Blog post-->
                            <div class="card mb-4">
                                <a href="#!"><img class="card-img-top" src="https://dummyimage.com/700x350/dee2e6/6c757d.jpg" alt="..." /></a>
                                <div class="card-body">
                                    <div class="small text-muted">January 1, 2022</div>
                                    <h2 class="card-title h4">Post Title</h2>
                                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla.</p>
                                    <a class="btn btn-primary" href="#!">Read more →</a>
                                </div>
                            </div>
                            <!-- Blog post-->
                            <div class="card mb-4">
                                <a href="#!"><img class="card-img-top" src="https://dummyimage.com/700x350/dee2e6/6c757d.jpg" alt="..." /></a>
                                <div class="card-body">
                                    <div class="small text-muted">January 1, 2022</div>
                                    <h2 class="card-title h4">Post Title</h2>
                                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla.</p>
                                    <a class="btn btn-primary" href="#!">Read more →</a>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6">
                            <!-- Blog post-->
                            <div class="card mb-4">
                                <a href="#!"><img class="card-img-top" src="https://dummyimage.com/700x350/dee2e6/6c757d.jpg" alt="..." /></a>
                                <div class="card-body">
                                    <div class="small text-muted">January 1, 2022</div>
                                    <h2 class="card-title h4">Post Title</h2>
                                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla.</p>
                                    <a class="btn btn-primary" href="#!">Read more →</a>
                                </div>
                            </div>
                            <!-- Blog post-->
                            <div class="card mb-4">
                                <a href="#!"><img class="card-img-top" src="https://dummyimage.com/700x350/dee2e6/6c757d.jpg" alt="..." /></a>
                                <div class="card-body">
                                    <div class="small text-muted">January 1, 2022</div>
                                    <h2 class="card-title h4">Post Title</h2>
                                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla? Quos cum ex quis soluta, a laboriosam.</p>
                                    <a class="btn btn-primary" href="#!">Read more →</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Pagination-->
                    <nav aria-label="Pagination">
                        <hr class="my-0" />
                        <ul class="pagination justify-content-center my-4">
                            <li class="page-item disabled"><a class="page-link" href="#" tabindex="-1" aria-disabled="true">Newer</a></li>
                            <li class="page-item active" aria-current="page"><a class="page-link" href="#!">1</a></li>
                            <li class="page-item"><a class="page-link" href="#!">2</a></li>
                            <li class="page-item"><a class="page-link" href="#!">3</a></li>
                            <li class="page-item disabled"><a class="page-link" href="#!">...</a></li>
                            <li class="page-item"><a class="page-link" href="#!">15</a></li>
                            <li class="page-item"><a class="page-link" href="#!">Older</a></li>
                        </ul>
                    </nav>
                </div>
                <!-- Side widgets-->
                <div class="col-lg-4">
                    <!-- Search widget-->
                    <div class="card mb-4">
                        <div class="card-header">Search</div>
                        <div class="card-body">
                            <div class="input-group">
                                <input class="form-control" type="text" placeholder="Enter search term..." aria-label="Enter search term..." aria-describedby="button-search" />
                                <button class="btn btn-primary" id="button-search" type="button">Go!</button>
                            </div>
                        </div>
                    </div>
                    <!-- Categories widget-->
                    <div class="card mb-4">
                        <div class="card-header">Categories</div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-sm-6">
                                    <ul class="list-unstyled mb-0">
                                        <li><a href="#!">Web Design</a></li>
                                        <li><a href="#!">HTML</a></li>
                                        <li><a href="#!">Freebies</a></li>
                                    </ul>
                                </div>
                                <div class="col-sm-6">
                                    <ul class="list-unstyled mb-0">
                                        <li><a href="#!">JavaScript</a></li>
                                        <li><a href="#!">CSS</a></li>
                                        <li><a href="#!">Tutorials</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Side widget-->
                    <div class="card mb-4">
                        <div class="card-header">Side Widget</div>
                        <div class="card-body">You can put anything you want inside of these side widgets. They are easy to use, and feature the Bootstrap 5 card component!</div>
                    </div>
                </div>
            </div>
      </div>
        <!-- Footer-->
        <footer class="py-5 bg-dark">
            <div class="container"><p class="m-0 text-center text-white">Construido por &copy; {{configuracion.construido_por}}</p></div>
        </footer>
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
    </body>
</html>
```

- Dentro de ```ejemplo/templates/ejemplo``` creamos un archivo HTML en nuestro caso ```base.html``` y copiamos lo siguiente:

```HTML
<!DOCTYPE html>
<html lang="es">

<head>
    {% load static %}
    {% load crispy_forms_tags %}
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!--Core themeCSS -->
    <link href="{% static 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css' %}" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script> 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.min.js" integrity="sha384-IDwe1+LCz02ROU9k972gdyvl+AESN10+x7tBKgc9I5HFtuNz0wWnPclzo6p9vxnk" crossorigin="anonymous"></script>
 

    <title>Martín Maddalena - Johan Romero</title>
</head>

<body>
    <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
          <a class="navbar-brand" href="    {% url 'Inicio' %}  ">Pagina Inicial</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">

            <ul class="navbar-nav me-auto mb-2 mb-lg-0">

                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'Alta' %} ">Cargar Familiar</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'Buscar' %}">Buscar Familiar</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'Lista' %}">Ver Familiar</a>
                </li>

            </ul>

          </div>
        </div>
      </nav>
    </header>
    <div class="div_1" >
        <div class ="content container">
            
        <h2>{% block titulo %} {% endblock %}<h2>
        <h3>{% block contenido %} {% endblock %}</h3>
    </div>
    </div>
 
</body>

</html>
```

- Dentro de proyecto_coderhouse ingresamos al archivo ```settings.py``` y hacemos algunos cambios:

```Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ejemplo.apps.EjemploConfig', #agregamos APP EJEMPLO
    'blog.apps.BlogConfig', # agregamos APP BLOG
    'crispy_forms' #INGRESAMOS pip install django_crispy-forms
]
CRISPY_TEMPLATE_PACK = 'bootstrap4' #agregamos complemento de crispy.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```

- ```crispy-forms``` sirve para leer correctamente las plantillas del bootstrap4.

## En la carpeta: ```ejemplo/Models.py```

- Realizar el import ```from django.db import models``` y crear la siguiente clase: 

```Python

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_de_nacimiento = models.DateField()
    numero_pasaporte = models.IntegerField()
    
def __str__(self):
    return f"{self.nombre}, {self.apellido}, {self.direccion}, {self.email}, {self.fecha_de_nacimiento}, {self.numero_pasaporte}, {self.id}"

```

- Creamos una clase y agregamos variables para generar un formulario poco estetico que va a estar conectado a la ```db, forms, views, 0001 y admin```

## En la carpeta: ```blog/Models.py```

- Realizar el import ```from django.db import models```y tambien importamos ```from traitlets import default``` y crear la siguiente clase: 

```Python

from traitlets import default

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=20)
    construido_por = models.CharField(max_length=30)
    titulo_principal = models.CharField(max_length=30, default='')
    subtitulo_principal = models.CharField(max_length=70, default='')

```

- Creamos una clase y agregamos variables para generar un acceso rapido a las configuraciones basicas desde el ```admin``` que va a estar conectado al ```index.html```

### En la carpeta ```ejemplo/``` creamos un nuevo archivo llamado ```forms.py``` realizamos algunos imports nuevos y ademas agregamos 2 clases.

```python
from cProfile import label # Predeterminada de Django
from django import forms # Predeterminada de Django
from ejemplo.models import Familiar #Funcion que creamos models

class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100) #Para buscar usuario por "nombre"

class FamiliarForm(forms.ModelForm): # Realiza un formulario basico que luego se lo pasamos a HTML
  class Meta:
    model = Familiar
    fields = [
      'nombre',
      'apellido',
      'direccion', 
      'email',
      'fecha_de_nacimiento', 
      'numero_pasaporte' 
    ]
    widgets = {
      'nombre':forms.TextInput(attrs={'placeholder':'Nombre'}),
      'apellido':forms.TextInput(attrs={'placeholder':'Apellido'}),
      'direccion':forms.TextInput(attrs={'placeholder':'direccion'}),
      'email':forms.EmailInput(attrs={'placeholder':'ejemplo@gmail.com'}),
      'fecha_de_nacimiento': forms.DateInput(attrs={'type':'date'}),
      'numero_pasaporte':forms.NumberInput(attrs={'placeholder':'Pasaporte N°'})
      }
``` 

### En la carpeta ```ejemplo/views.py``` hacemos los imports y creamos las funciones que nos van ayudar a realizar busquedas, mostrar un listado por pantalla y registrar nuevos datos.

```python
from django.shortcuts import render # Predeterminada de Django
from ejemplo.models import Familiar # importamos las clases de models.py
from ejemplo.forms import Buscar, FamiliarForm # importamos las clases de forms.py
from django.views import View # Predeterminada de Django


def monstrar_familiares(request): # Hace una lista los familiares
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View): # Para realizar las busquedas de familiares
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":"Nombre a buscar"}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View): # Para registrar los nuevos familiares

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "apellido":"", "direccion":"", "email":"", "fecha_de_nacimiento":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se cargo con éxito el familiar {form.cleaned_data.get('nombre')} !!!"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})   

``` 

### Dentro de ``` proyecto_coderhouse/urls.py``` agregamos los imports y las rutas para que se muestren por pantalla de la siguiente manera:

```python
from django.contrib import admin
from django.urls import path
from ejemplo.views import (monstrar_familiares, BuscarFamiliar, 
                           AltaFamiliar) # SE AGREGAN TODAS LAS CLASES DE EJEMPLO/VIEWS.PY
from blog.views import index as blog_index # SE AGREGAN TODAS LAS CLASES DE BLOG/VIEWS.PY


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_index, name="Inicio"), # RUTA PARA INDEX.HTML
    path('mi-familia/', monstrar_familiares, name="Lista"), # RUTA PARA MOSTRAR LOS FAMILIARES
    path('mi-familia/buscar', BuscarFamiliar.as_view(), name="Buscar"), # RUTA PARA BUSCAR UN FAMILIAR
    path('mi-familia/alta', AltaFamiliar.as_view(), name="Alta"), # RUTA DEL FORMULARIO PARA GUARDAR UN FAMILIAR NUEVO
]
```

# Creamos los siguientes templates:

- En todos nuestros templates debemos heredar nuestro archivo ```base.html``` de la siguiente manera:

```html
{% extends 'ejemplo/base.html' %}
```

- Para realizar el alta de usuario/familiar vamos vamos a crear ```alta_familiar.html``` en la siguiente ruta ```templates/ejemplo/alta_familiar.html```

```html

{% extends 'ejemplo/base.html' %} <!-- Se utiliza {% extends 'ejemplo/base.html' %} para tomar la estructura/maquetado del base.html -->


{% block contenido %}<!-- Utilizamos un bloque en donde debemos  ingresar el contenido que contendra nuestro html-->
<center>
  <h1>Alta de nuevo Familiar</h1>
<section class="sec_alta_fam" >

  <form class="row g-12"  method="post">
  {% csrf_token %} <!-- protege ante falsificacion de solicitudes de otras fuentes. -->

    <div class="col-md-12"> 
      {{form.nombre}} {{form.apellido}}<!-- cargar nuestros datos-->
    </div>
    <p></p>


      
    <div class="col-md-12">    
      {{form.direccion}} {{form.email}}

    </div>
    <p></p>
 

    <div class="col-md-24"> 
      {{form.numero_pasaporte}}
    </div>
    <p></p>
    <div class="col-md-12">  
      {{form.fecha_de_nacimiento}}
    </div>
    <p></p>

    <div class="col-12">
      <button type="submit" class="btn btn-warning">Cargar Nuevo</button><!-- boton para cargar datos -->
    </div>

  </form>

  <h3 class="msg_exito">{{msg_exito}}</h3>

</section>
</center>
   {% endblock %} <!-- cerramos el bloque -->
```

- Para las busquedas de usuarios/familiares vamos a crear ```buscar.html``` en la siguiente ruta ```templates/ejemplo/buscar.html```

```HTML

<!DOCTYPE html>
  <html lang="es">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Romero - Maddalena</title>
  </head>
  <body>
    {% extends 'ejemplo/base.html' %}
    
    {% block contenido %}
    <div class="container"> 
      <center><h1>Buscar por nombre</h1>
      <form action="/mi-familia/buscar" method="post"><!-- utilizamos metodo post para mandar y traer a la db -->
        {% csrf_token %}<!-- protege. -->
        <div>{{ form }}</div><!--guarda-->
        <div><input type="submit" class="btn btn-warning"></div>
      </form>
    
      <table class="table">
         <thead>
         <tr>
             <th scope="col">ID</th>
             <th scope="col">Nombre</th>
             <th scope="col">Apellido</th>
             <th scope="col">Documento</th>
             <th scope="col">Email/Correo</th>
             <th scope="col">Direccion</th>
             <th scope="col">Nacimiento</th>
         </tr>
         </thead>
         <tbody class="table-group-divider">
     
         {% for user in lista_familiares %} <!--FILTRA-->
             <tr>
                 <th scope="row">{{ user.id }}</th><!-- Muestra datos del usuario que buscamos-->
                 <td>{{ user.nombre}}</td>
                 <td>{{ user.apellido }}</td>
                 <td>{{ user.numero_pasaporte }}</td>
                 <td>{{ user.email }}</td>
                 <td>{{ user.direccion }}</td>
                 <td>{{ user.fecha_de_nacimiento }}</td>
             </tr>
             
             
             
         {% endfor %} <!-- finalizamos for -->
    {% endblock %}
  </center>
  </div>
  </body>
  </html>

```

- Para ver los usuarios/familiares cargados en la db vamos a crear ```familiares.html``` en la siguiente ruta ```templates/ejemplo/familiares.html```

```html

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maddalena - Romero</title>
</head>
<body>
 {% extends 'ejemplo/base.html' %}
 {% block titulo%} Lista de todos mis Familiares {% endblock %}
 {% block contenido %}
 <table class="table">
    <thead>
    <tr>
        <th scope="col">ID</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido</th>
        <th scope="col">Documento</th>
        <th scope="col">Email/Correo</th>
        <th scope="col">Direccion</th>
        <th scope="col">Nacimiento</th>
    </tr>
    </thead>
    <tbody class="table-group-divider">

    {% for user in lista_familiares %}
        <tr>
            <th scope="row">{{ user.id }}</th>
            <td>{{ user.nombre}}</td>
            <td>{{ user.apellido }}</td>
            <td>{{ user.numero_pasaporte }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.direccion }}</td>
            <td>{{ user.fecha_de_nacimiento }}</td>
        </tr>
        
        
        
    {% endfor %}
{% endblock %}
</body>
</html>

```

- Recordemos que podemos utilizar el archivo seed_data.py para cargar usuarios mediante el ```shell``` comando: ``` python manage.py shell ```

- Luego en la consola de visual estudio code vamos a ejecutar el script de la siguiente manera:

Esta opción solo funciona en terminal bash:

```bash
python manage.py shell < seed_data.py
```
Para un terminal cmd o powershell, tienen que hacer, primero:
```cmd
python manage.py shell
```
una vez que estan en el shell hacer:

```python
import seed_data
```
al finalizar, para ambos casos, se tiene que ver un msj que diga: 
```
Se cargo con éxito los usuarios de pruebas
```

## Por ejemplo:

```Python
from ejemplo.models import Familiar # El import trae las variables

Familiar(nombre = "Rosario", apellido = "Garcia", direccion ="Rio Parana 745", email = "rogarcia@gmail.com", fechaNac = "1920-12-5", numero_pasaporte = 123123).save() #  El .save() guarda en la base de datos

Familiar(nombre="Romina", apellido= "Londo", direccion="Melo 3790", email= "londoromi@gmail.com", fechaNac = "1930-7-15", numero_pasaporte=454545).save()

Familiar(nombre="Carlos", apellido= "Mario", direccion="Venezuela 840", email= "Carlos_Mario@gmail.com", fechaNac = "1940-9-20", numero_pasaporte=123123).save()


print("Se cargo con éxito los usuarios de pruebas")

```


- Para guardar los cambios en github:

  ```git add .```
  
  ```git commit -m "El mensaje que quieras"```
  
  ```git push origin main```
