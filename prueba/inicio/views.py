from django.shortcuts import render, HttpResponse
from .models import Alumnos
from inicio import views as views_registros
# Create your views here.

menu = """
    
"""

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'registros/principal.html', {'alumnos': alumnos, 'menu': menu})

def principal(request):
    return render(request, 'registros/principal.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')

def formulario(request):
    return render(request, 'inicio/formulario.html')

def ejemplo(request):
    return render(request, 'inicio/ejemplo.html')
 