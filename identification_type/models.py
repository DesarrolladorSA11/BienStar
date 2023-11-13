from django.db import models

class Identification_type(models.Model):
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
