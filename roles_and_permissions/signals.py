from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Rol

@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    if sender.name == 'roles_and_permissions':
        roles = [
            {'name': 'Administrador', 'code': 'ADMINISTRADOR'},
            {'name': 'Coordinador', 'code': 'COORDINADOR'},
            {'name': 'Estudiante', 'code': 'ESTUDIANTE'},
            {'name': 'Docente', 'code': 'DOCENTE'},
        ]

        for role_data in roles:
            Rol.objects.get_or_create(**role_data)
