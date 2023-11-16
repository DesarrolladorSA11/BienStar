from .models import AdminUser
from users_generics.models import CustomUser, Users
from .serializer import AdminUserSerializer, CustomUserSerializer, CreateUserSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer


from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render, redirect
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

from rest_framework.authtoken.views import ObtainAuthToken

# Token
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            'success': True,
            'message': 'Login successful',
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
        }

        return Response(response_data, status=status.HTTP_200_OK)


# Admin - Litar
class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


# Admin - Sign up
class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action == 'list':
            return [IsAuthenticated()]
        return super().get_permissions()




# Admin - Login Json 
"""
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/api1/list/')
        else:
            return super(LoginAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            request.auth = token
            return HttpResponseRedirect('/api1/list/')
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
"""

"""
# Admin - Login Json
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list')

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            request.auth = token
            return redirect('list')
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
"""
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({
                'success': True,
                'message': 'Login successful',
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
            })
        else:
            return Response({
                'success': False,
                'message': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)


# Admin - Logout
class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)
    

# Admin - Create Users
class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = CreateUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action == 'list':
            return [IsAuthenticated()]
        return super().get_permissions()
    
"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action == 'list':
            return [IsAuthenticated()]
        return super().get_permissions()
 """