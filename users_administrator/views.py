from .models import AdminUser
from .serializer import AdminUserSerializer #, AdminUserLoginSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate


# Create
class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]
        return super().get_permissions()



"""
# Auth
class AdminUserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AdminUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            print(f'Username: {username}, Password: {password}')

            # Autenticar al usuario
            admin_user = authenticate(username=username, password=password)
            if admin_user:
                # Generar tokens de acceso y actualización
                refresh = RefreshToken.for_user(admin_user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""