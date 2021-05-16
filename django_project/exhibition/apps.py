from django.apps import AppConfig


class ExhibitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_project.exhibition'

    def ready(self):
        import django_project.exhibition.signals
