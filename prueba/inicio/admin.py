from django.contrib import admin
from .models import Alumnos

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'carrera', 'turno', 'created', 'updated')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    list_filter = ('turno',)
    ordering = ('-created',)
# Register your models here.
