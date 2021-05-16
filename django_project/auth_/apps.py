from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_project.auth_'

    def ready(self):
        import django_project.auth_.signals
