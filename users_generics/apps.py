from django.apps import AppConfig


class UsersGenericsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_generics'

    def ready(self):
        import users_generics.signals