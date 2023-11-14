from .models import AdminUser
from users_generics.models import CustomUser
from .serializer import AdminUserSerializer, CustomUserSerializer

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.shortcuts import render,redirect
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

# Litar
class UsersList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


# Create
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
        

# Login - html
class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)


# Login Json       
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)