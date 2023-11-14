from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet, UsersList, Logout , LoginAPIView #,  Login
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'', AdminUserViewSet)


urlpatterns = [
    path('sigin/', include(router.urls)),
    path('token/', views.obtain_auth_token),
    path('list/', UsersList.as_view(), name = 'list'),
    #path('login/', Login.as_view(), name = 'login'),
    path('login2/',LoginAPIView.as_view(), name = 'login2'),
    path('logout/', Logout.as_view(), name = 'logout'),
]


