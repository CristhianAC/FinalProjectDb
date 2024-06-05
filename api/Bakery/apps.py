from django.apps import AppConfig


class BakeryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bakery'
    def ready(self):
        import Bakery.signals