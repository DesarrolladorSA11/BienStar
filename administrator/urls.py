from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'', AdminUserViewSet)

urlpatterns = [
    path('create/', include(router.urls)),
    path('token/', views.obtain_auth_token),
]
