from .models import AdminUser
from users_generics.models import CustomUser, Users
from rest_framework import serializers


class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = AdminUser
        fields = ('id', 'username', 'password', 'name', 'last_name', 'email', 'cellphone', 'identification_number', 'id_identification_type')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        identification_type = validated_data.pop('id_identification_type', None)

        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        if identification_type is not None:
            instance.id_identification_type = identification_type

        instance.save()
        return instance

# 
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'name',
            'identification_number',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'last_name', 'email', 'cellphone', 'identification_number', 'id_identification_type', 'id_rol')

    def create(self, validated_data):
        identification_type = validated_data.pop('id_identification_type', None)
        rol_type = validated_data.pop('id_rol', None)

        instance = self.Meta.model(**validated_data)

        if identification_type is not None:
            instance.id_identification_type = identification_type
        
        if rol_type is not None:
            instance.id_rol = rol_type

        instance.save()
        return instance
