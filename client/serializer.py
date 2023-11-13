"""from rest_framework import serializers
from .models import Profile, User
"""
"""
#ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'status', 'name', 'last_name', 'email', 'cellphone', 'identification_number')


#UserSeializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'password')

"""