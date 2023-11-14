from .models import AdminUser
from rest_framework import serializers

class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = AdminUser
        fields = ['id', 'username', 'password', 'status', 'name', 'last_name', 'email', 'cellphone', 'identification_number', 'id_identification_type']

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


    
"""
class AdminUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)
    
"""