from django.contrib.auth.models import AbstractUser
from django.db import models

# MODEL - DEFAULT
class CustomUser(AbstractUser):
    status = models.BooleanField(default=True)
    identification_number = models.CharField(max_length=10, unique=True, null=False)
    cellphone = models.CharField(null=False, blank=False, max_length=10)
    name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    
    def __str__(self):
        return self.name

# ROLES
class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=100)
    rol_type = [
        ('Administrador', 'Administrador'),
        ('Coordinador', 'Coordinador'),
        ('Estudiante', 'Estudiante'),
        ('Docente', 'Docente'),
    ]
    name = models.CharField(max_length=100, choices=rol_type)

    def __str__(self):
        return self.name
    

# IDENTIFICATION_TYPE
class Id_type(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=100)
    id_type = [
        ('CC', 'CC'),
        ('Cedula Extranjera', 'Cedula Extranjera'),
        ('Pasaporte', 'Pasaporte'),
        ('Tarjeta Identidad', 'Docente'),
    ]
    name = models.CharField(max_length=100, choices=id_type)

    def __str__(self):
        return self.name


# USERS 
class Users(CustomUser):
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True, related_name='user_id_rol')
    id_identification_type = models.ForeignKey(Id_type, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_dentification_type')

    def __str__(self):
        return self.name
