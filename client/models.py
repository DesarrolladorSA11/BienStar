from django.db import models

"""
# IDENTIFICATION_TYPE
class Identification_type(models.Model):
    #code = models.CharField(unique=True, max_length=100)
    identification_type = [
        ('C.C', 'C.C'),
        ('Cedula Extranjera', 'Cedula Extranjera'),
        ('Tarjeta Identidad', 'Tarjeta Identidad'),
        ('Pasaporte', 'Pasaporte'),
    ]
    name = models.CharField(max_length=100, choices=identification_type)

    def __str__(self):
        return self.name

    
# ROL
class Rol(models.Model):
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


# PROFILE
class Profile(models.Model):
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    cellphone  = models.CharField(null=False, blank=False, unique=True, max_length=15)
    identification_number = models.CharField(max_length=20, unique=True)

    #id_identification_type = models.ForeignKey(Identification_type, on_delete=models.CASCADE, related_name="profile_rol")
    #id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="profile_rol")

    def __str__(self):
        return self.name
    

# USER
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    id_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_profile")

    def __str__(self):
        return self.name



# PERMISSION
class Permission(models.Model):
    code = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ROL_PERMISSION
class Rol_permission(models.Model):

    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="rol_permission_profile")
    id_permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name="rol_permission_permission")

"""