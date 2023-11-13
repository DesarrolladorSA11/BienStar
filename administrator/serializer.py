from rest_framework import serializers
from .models import AdminUser

class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AdminUser
        fields = ['id', 'username', 'password', 'status', 'name', 'last_name', 'email', 'cellphone', 'identification_number']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
"""
class AdminUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)
    
"""