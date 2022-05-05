from .views import UserRegisterView
from django.urls import path
from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
]
