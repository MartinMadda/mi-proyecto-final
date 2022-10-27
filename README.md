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
