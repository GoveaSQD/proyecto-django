from django.shortcuts import render, redirect
from inicio.models import Alumnos
from .forms import ComentarioContactoForm, FormArchivos
from .models import Archivos
from registros.models import ComentarioContacto
from django.shortcuts import get_object_or_404
from django.contrib import messages
import datetime
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
 
def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentarios_contacto')  # Redirige a la vista de comentarios
    else:
        form = ComentarioContactoForm()
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):

    return render(request,"registros/contacto.html")
#Indicamos el lugar donde se renderizará el resultado de esta vista

def comentarios_contacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'inicio/comentarios.html', {'comentarios': comentarios})

def eliminarComentarioContacto(request, id, confirmacion='registros/eliminarComentario.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        return redirect('comentarios_contacto')  # Redirige a la tabla de comentarios
    return render(request, 'registros/eliminarComentario.html', {'object': comentario})

def consultar1(request):
    #con unsa sola condicion
    alumnos = Alumnos.objects.filter(carrera='TI')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar2(request):
    #con unsa sola condicion
    alumnos = Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar3(request):
    #si solo deseamos recuperar ciertos datos agregamos la funcion only, listando los campos que queremos obtener de la consulta emplear filter o en el ejemplo all()
    alumnos = Alumnos.objects.all().only('matricula', 'nombre', 'carrera', 'turno', 'imagen')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar4(request):
    alumnos= Alumnos.objects.filter(turno__contains='Vesp')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar5(request):
    alumnos= Alumnos.objects.filter(nombre__in=['Juan', 'Ana'])
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2025, 6, 1)
    fechaFin = datetime.date(2025, 6, 25)
    alumnos= Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})

def consultar7(request):
    #consultando entre modelos
    alumnos= Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})
#en comentarios contacto

def consultar8(request):
    #comentarios entre 8 y 9 de julio
    fechaInicio = datetime.date(2025, 7, 7)
    fechaFin = datetime.date(2025, 7, 10)
    comentarios = ComentarioContacto.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def consultar9(request):
    #consulta que busca una expresion en el comentario
    comentarios = ComentarioContacto.objects.filter(mensaje__contains='Mensaje de prueba')
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def consultar10(request):
    #consulta que pertenece a un usuario
    comentarios = ComentarioContacto.objects.filter(usuario__iexact='aLe')
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def consultar11(request):
    #consulta que returne solamente comentarios
    comentarios = ComentarioContacto.objects.all().only('mensaje', 'usuario')
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def consultar12(request):
    #consulta diferente a todas las anteriores
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains='ComEntarIo')
    return render(request, 'registros/comentarios.html', {'comentarios': comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo=request.POST['titulo']
            descripcion=request.POST['descripcion']
            archivo=request.FILES['archivo']
            insert= Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render (request, 'registros/archivos.html')
        else:
            messages.error(request, 'Error al procesar el formulario.')
    else:
            return render(request, 'registros/archivos.html', {'archivo': Archivos})

def consultasSQL(request):

    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno, imagen FROM inicio_alumnos WHERE carrera="TI" ORDER BY turno DESC')

    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def seguridad(request):
    nombre = request.GET.get('nombre')
    return render(request, 'registros/seguridad.html', {'nombre': nombre})
 