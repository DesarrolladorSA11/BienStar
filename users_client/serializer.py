from .models import ClientUser
from rest_framework import serializers

class ClientUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = ClientUser
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
from rest_framework import serializers
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