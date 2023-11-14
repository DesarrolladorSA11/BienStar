from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Rol, Id_type


@receiver(post_migrate)
def load_initial_data_rol(sender, **kwargs):
    if sender.name == 'users_generics':
        roles = [
            {'name': 'Administrador', 'code': 'ADMINISTRADOR'},
            {'name': 'Coordinador', 'code': 'COORDINADOR'},
            {'name': 'Estudiante', 'code': 'ESTUDIANTE'},
            {'name': 'Docente', 'code': 'DOCENTE'},
        ]

        for role_data in roles:
            Rol.objects.get_or_create(**role_data)


@receiver(post_migrate)
def load_initial_data_idtype(sender, **kwargs):
    if sender.name == 'users_generics':
        ids = [
            {'name': 'CC', 'code': 'CC'},
            {'name': 'Cedula Extranjera', 'code': 'CEDULA EXTRANJERA'},
            {'name': 'Pasaporte', 'code': 'PASAPORTE'},
            {'name': 'Tarjeta Identidad', 'code': 'TARJETA IDENTIDAD'},
        ]

        for id_data in ids:
            Id_type.objects.get_or_create(**id_data)
