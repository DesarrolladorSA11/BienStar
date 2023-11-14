from users_generics.models import CustomUser
from django.db import models
from users_generics.models import Rol, Id_type

class ClientUser(CustomUser):
    #id = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='cliente_id_rol')
    id_identification_type = models.ForeignKey(Id_type, on_delete=models.SET_NULL, null=True, blank=True, related_name='cliente_id_identification_type')

    def save(self, *args, **kwargs):
        if not self.id_rol_id:
            docente_rol = Rol.objects.get(name='Docente')
            self.id_rol = docente_rol

        super().save(*args, **kwargs)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.name)