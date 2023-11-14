from users_generics.models import CustomUser
from django.db import models
from users_generics.models import Rol, Id_type

class AdminUser(CustomUser):
    #id = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='admin_id_rol')
    id_identification_type = models.ForeignKey(Id_type, on_delete=models.SET_NULL, null=True, blank=True, related_name='admin_id_identification_type')

    def save(self, *args, **kwargs):
        if not self.id_rol_id:
            admin_role = Rol.objects.get(name='Administrador')
            self.id_rol = admin_role

        super().save(*args, **kwargs)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.name)


