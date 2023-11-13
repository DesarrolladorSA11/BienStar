from django.apps import AppConfig

class RolesAndPermissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'roles_and_permissions'

    def ready(self):
        import roles_and_permissions.signals
