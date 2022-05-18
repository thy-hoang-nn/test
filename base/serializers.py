from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ( 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user( validated_data['email'], validated_data['password'])

        return user

    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    def validate(self, data):
        email= data.get("email", None)
        password= data.get("password", None)
        print(email)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        return {
            'email':user.email
        }

    # def validate(self, data):
    #     user = authenticate(**data)
    #     print(data)
    #     print(user)
    #     if user and user.is_active:
    #         return user
    #     raise serializers.ValidationError('Incorrect Credentials Passed.')



    
    
