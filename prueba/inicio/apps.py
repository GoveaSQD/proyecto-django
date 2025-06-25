from django.apps import AppConfig


class InicioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inicio'

class RegistrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registros'    
    verbose_name = 'Modulos'
