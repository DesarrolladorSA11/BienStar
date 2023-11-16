from django.db import models
from users_generics.models import Rol

class UserClient(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    identification_number = models.CharField(max_length=10, unique=True, null=False)
    name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.EmailField()

    identification_type = models.CharField(max_length=20)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='users_client_id_rol')

    def __str__(self):
        return self.username