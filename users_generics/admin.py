from django.contrib import admin
from .models import Rol, Id_type, CustomUser

admin.site.register(CustomUser)
admin.site.register(Rol)
admin.site.register(Id_type)
