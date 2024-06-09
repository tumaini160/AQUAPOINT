from django.apps import AppConfig


class AquapointappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AQUAPOINTAPP'
    
    def ready(self):
        from .job import start
        start()
