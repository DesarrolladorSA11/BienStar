from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientUserViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'', ClientUserViewSet)

urlpatterns = [
    path('create/', include(router.urls)),
    path('token/', views.obtain_auth_token),
]


"""
from django.urls import path
from rest_framework import routers
from client import views
"""
"""
#Routers
router = routers.DefaultRouter()
router.register(r'profile', views.ProfileView, 'profile')
router.register(r'user', views.UserView, 'user')


#Api V..
urlpatterns = [
    path("Apiv1/", include(router.urls)),
]
"""
"""
from .views import ldap_authenticate

urlpatterns = [
    path('api1/', ldap_authenticate, name='ldap_authenticate'),
]"""