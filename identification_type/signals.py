from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Identification_type

@receiver(post_migrate)
def load_initial_data(sender, **kwargs):
    if sender.name == 'identification_type':
        ids = [
            {'name': 'CC', 'code': 'CC'},
            {'name': 'Cedula Extranjera', 'code': 'CEDULA EXTRANJERA'},
            {'name': 'Pasaporte', 'code': 'PASAPORTE'},
            {'name': 'Tarjeta Identidad', 'code': 'TARJETA IDENTIDAD'},
        ]

        for id_data in ids:
            Identification_type.objects.get_or_create(**id_data)
