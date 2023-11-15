from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminUserViewSet, UsersList, Logout , LoginAPIView, CreateUserViewSet, CustomObtainAuthToken
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'signup', AdminUserViewSet, basename='signup')
router.register(r'createuser', CreateUserViewSet, basename='createuser')


urlpatterns = [
    path('', include(router.urls)),
    
    path('token/', views.obtain_auth_token),
    path('tokenurl/', CustomObtainAuthToken.as_view(), name='token_obtain'),
    path('login/', LoginAPIView.as_view(), name = 'login'),
    path('list/', UsersList.as_view(), name = 'list'),
    path('logout/', Logout.as_view(), name = 'logout'),
]


