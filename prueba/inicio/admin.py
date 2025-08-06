from django.contrib import admin
from .models import Alumnos
from .models import Comentario
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('matricula','nombre','carrera','turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

admin.site.register(Alumnos, AdministrarModelo)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created', 'updated')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    list_filter = ('turno',)
    ordering = ('-created',)
# Register your models here.

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Comentario, AdministrarComentarios)
