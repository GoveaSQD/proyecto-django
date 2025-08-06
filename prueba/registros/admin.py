from django.contrib import admin
from .models import ComentarioContacto

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    

admin.site.register(ComentarioContacto, AdministrarComentariosContacto)
