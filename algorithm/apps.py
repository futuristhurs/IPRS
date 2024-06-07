from django.apps import AppConfig


class AlgorithmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'algorithm'
    
    def ready(self):
        from .management_commands import import_data
        self.stdout.write(self.style.SUCCESS(F'importing {import_data.ImportDataCommand. __name__} command'))