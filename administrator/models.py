from django.contrib.auth.models import AbstractUser
from django.db import models
from roles_and_permissions.models import Rol

class AdminUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    cellphone = models.CharField(null=False, blank=False,max_length=10)
    identification_number = models.CharField(max_length=10, unique=True, null=False)

    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id_rol_id:
            admin_role = Rol.objects.get(name='Administrador')
            self.id_rol = admin_role

        super().save(*args, **kwargs)

    def __str__(self):
        return '{0},{1}'.format(self.last_name, self.name)
