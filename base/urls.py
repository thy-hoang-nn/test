from .views import  UserRegisterView
from django.urls import path
from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    # path('login', SignInAPI.as_view(), name='token_obtain_pair'),
    # path('token/obtain/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
