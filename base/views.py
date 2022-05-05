from django.shortcuts import render

# Create your views here.
# from django.http import JsonResponse
from rest_framework.views import APIView

from .serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response



class UserRegisterView(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
       
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(
                serializer.validated_data['password'])
            user = serializer.save()

            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'True',
                'status code': status_code,
                'message': 'User registered  successfully',
            }
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'status_code': status_code,
                'error_message': 'This email has already exist!',
            }

        return Response(response, status=status_code)
