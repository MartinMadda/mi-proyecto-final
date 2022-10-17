from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html")

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html",
    {
        "nombre": nombre,
        "apellido": apellido,
    })