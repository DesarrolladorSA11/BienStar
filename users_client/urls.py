# ldap_api/urls.py

from django.urls import path
from .views import LDAPAuthAPIView

urlpatterns = [
    path('ldap/', LDAPAuthAPIView.as_view(), name='ldap'),
]
