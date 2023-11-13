from django.apps import AppConfig


class IdentificationTypeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'identification_type'

    def ready(self):
        import identification_type.signals