from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet

router = DefaultRouter()
router.register(r'adminusers', AdminUserViewSet)

urlpatterns = [
    path('api2/', include(router.urls)),
]
