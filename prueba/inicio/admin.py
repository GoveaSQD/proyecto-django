from django.contrib import admin
from .models import Alumnos
from .models import Comentario

admin.site.site_header = "Mi Administración Personalizada"
admin.site.site_title = "Sitio de Admin"
admin.site.index_title = "Bienvenido al Panel de Control"

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('matricula','nombre','carrera','turno', 'created', 'updated')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
    list_per_page = 2
    list_display_links = ('matricula', 'nombre')
    list_editable = ('carrera', 'turno')

    def get_readonly_fields(self, request, obj=None):
        #si el usuario pertence al grupo de permisos "Alumnos"
        if request.user.groups.filter(name='Alumnos').exists():
            #bloquea los campos
            return ('created', 'updated', 'matricula', 'carrera', 'turno')
            #Cualquier otro usuario que no pertenece al grupo "Alumnos"
        else:
            #no bloquea los campos
            return ('created', 'updated')
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Grupo de Comentaristas').exists():
            #bloquea los campos de comentario incluyendo el nombre del alumno y asi solo pueda modificar
            return ('created', 'updated', 'nombre', 'matricula', 'carrera', 'turno')
        else:
            return ('created', 'updated')

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
