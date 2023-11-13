from django.db import models

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
