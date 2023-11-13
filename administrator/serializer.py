from rest_framework import serializers
from .models import AdminUser

class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Esto agrega un campo de contraseña al serializer

    class Meta:
        model = AdminUser
        # Lista de campos específicos que deseas incluir en el serializer
        fields = ['id', 'username', 'password', 'status', 'name', 'last_name', 'email', 'cellphone', 'identification_number']

    def create(self, validated_data):
        # Extraes la contraseña del diccionario validado y la estableces usando el método set_password
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
