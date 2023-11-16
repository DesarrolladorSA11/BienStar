
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


from .models import UserClient
from .serializers import UserClientSerializer

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

import os
from ldap3 import Server, Connection, ALL

from dotenv import load_dotenv
load_dotenv()

ldap_opts = os.getenv('LDAPOPTS')
admin_dn = os.getenv('ADMINDN')
user_search_base = os.getenv('USERSEARCHBASE')
admin_password = os.getenv('ADMINPASSWORD')


class LDAPBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        server = Server(ldap_opts, get_info=ALL)

        with Connection(server, user=admin_dn, password=admin_password, auto_bind=True) as conn:
            search_filter = f'(&(uid={username}))'

            conn.search(user_search_base, search_filter, attributes=['sinuUser', 'cn', 'objectClass', 'userPassword', 'uid', 'displayName', 'sn', 'givenName', 'mail'])

            entry = conn.entries[0] if conn.entries else None

            if entry and conn.rebind(user=entry.entry_dn, password=password):
                User = get_user_model()
                user, created = User.objects.get_or_create(username=username)

                user.first_name = entry.givenName.value
                user.last_name = entry.sn.value
                user.email = entry.mail.value
                user.sinu = entry.sinuUser.value[0] if 'sinuUser' in entry else None
                user.save()

                return user

        return None


class LDAPAuthAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        
        try:
            sinu_user = UserClient.objects.get(username=username)
            serializer = UserClientSerializer(sinu_user)
            return Response({'detail': 'Ya existe el usuario'}, status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserClient.DoesNotExist:
            pass
        

        """
        try:
            sinu_user = UserClient.objects.get(username=username)
            
            if sinu_user.password == password:
                token, created = Token.objects.get_or_create(user=sinu_user)
                return Response({'token': token.key, 'user_id': sinu_user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
        except UserClient.DoesNotExist:
            # El usuario no existe, proceder con la autenticación y consultas LDAP
            pass
        """
        
        """
        ApiSinu = 'http://192.168.11.97/searches/consultar_perfil.json?periodos='
        ApiSinu = ApiSinu + username
        data = requests.get(ApiSinu)
        if data.status_code == 200:
            data_pefil = data.json()
            if data_pefil[0][3] == 'ALUMNO':
                rol = data_pefil[0][0]
        """

        if not username or not password:
            return Response({'error': 'Debe proporcionar un nombre de usuario y una contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        user = LDAPBackend().authenticate(request, username=username, password=password)

        if user:
            if user.sinu:
                # UserClient
                sinu_user, created = UserClient.objects.update_or_create(
                    username=user.username,
                    defaults={
                        'username': user.username,
                        'password': password, 
                        'identification_number': user.username,
                        'name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                        #'rol_type': 'rol',
                    }
                )

                serializer = UserClientSerializer(sinu_user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'El Usuario no pertenece a Sinu'}, status=status.HTTP_403_FORBIDDEN)

        return Response({'detail': 'Autenticación fallida'}, status=status.HTTP_401_UNAUTHORIZED)
