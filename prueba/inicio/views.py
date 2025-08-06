from django.shortcuts import render, HttpResponse
from .models import Alumnos
from registros.models import ComentarioContacto
from inicio import views as views_registros
from django.shortcuts import get_object_or_404
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

def ComentarioContacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'inicio/comentarios.html', {'comentarios': comentarios})

def eliminarComentarioContacto(request, id, confirmacion='inicio/eliminarComentario.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "inicio/comentarios.html", {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})

