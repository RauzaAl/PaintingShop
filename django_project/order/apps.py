from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_project.order'

    def ready(self):
        import django_project.order.signals
