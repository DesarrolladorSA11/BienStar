
"""
from .models import User, Profile
from rest_framework import viewsets, permissions
from .serializer import UserSerializer, ProfileSerializer

# ProfileView
class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# UserView
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
"""
"""
from ldap3 import Server, Connection, SIMPLE, SYNC, ALL, SUBTREE
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ldap_authenticate(request):
    ldap_opts = {'server': '190.60.75.134', 'port': 389}
    admin_dn = 'cn=manager,dc=americana,dc=edu,dc=co'
    user_search_base = 'ou=users,dc=americana,dc=edu,dc=co'
    admin_password = 'iceberg0'

    # Obtener credenciales del usuario desde la solicitud (ajústalo según tus necesidades)
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        # Crear conexión al servidor LDAP
        server = Server(ldap_opts['server'], port=ldap_opts['port'], get_info=ALL)
        connection = Connection(server, user=admin_dn, password=admin_password, auto_bind=True)

        # Construir la consulta de búsqueda
        search_filter = f'cn={username}'
        connection.search(user_search_base, search_filter, SUBTREE)

        # Verificar la contraseña
        if connection.response and connection.bind(user=connection.response[0]['dn'], password=password, version=3):
            return JsonResponse({'success': True, 'message': 'Autenticación exitosa'})
        else:
            return JsonResponse({'success': False, 'message': 'Credenciales inválidas'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error LDAP: {e}'})
"""