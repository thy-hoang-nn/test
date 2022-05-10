from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate

from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer


from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.urls import reverse
from .utils import Util
from .models import CustomUser

class UserRegisterView(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):     
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(
                serializer.validated_data['password'])
            user= serializer.save()
            user_data = serializer.data
            user = CustomUser.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relativeLink = reverse('email-verify')
            absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
            email_body = 'Hi '+user.username + \
            ' Use the link below to verify your email \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

            Util.send_email(data)   

        #     status_code = status.HTTP_201_CREATED
        #     response = {
        #         'success': 'True',
        #         'status code': status_code,
        #         'message': 'User registered  successfully',
        #     }
        # else:
        #     status_code = status.HTTP_400_BAD_REQUEST
        #     response = {
        #         'status_code': status_code,
        #         'error_message': 'This email has already exist!',
        #     }
      
        

        return Response(user_data, status=status.HTTP_201_CREATED)

#email verfication
@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view()
def complete_view(request):
    return Response("Email account is activated")









    
# class UserLoginView(APIView):
#     serializer_class = LoginSerializer
#     def post(self, request):
#         serializer = self.serializer_class(data= request.data)
#         if serializer.is_valid():
#             user =authenticate(
#                 request, 
#                 email= serializer.validated_data['email'],
#                 password = serializer.validated_data['password']
                
#             )
#             if user:
#                 refresh = TokenObtainPairSerializer.get_token(user)
#                 data = {
#                     'refresh_token': str(refresh),
#                     'access_token': str(refresh.access_token)
#                 }
#                 return Response(data, status=status.HTTP_200_OK)
#             return Response({
#                 'error_message': 'Email or password is incorrect!',
#                 'error_code': 400
#             }, status=status.HTTP_400_BAD_REQUEST)

#         return Response({
#             'error_messages': serializer.errors,
#             'error_code': 400
#         }, status=status.HTTP_400_BAD_REQUEST)
                
            
    
# class UserLoginView(APIView):
    
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         response = {
#             'success' : 'True',
#             'status code' : status.HTTP_200_OK,
#             'message': 'User logged in  successfully',
#             'token' : serializer.data['token'],
#             }
#         status_code = status.HTTP_200_OK

#         return Response(response, status=status_code)


# class SignInAPI(APIView):

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             get_user_model().objects.create_user(**serializer.validated_data)
#             return Response(status.HTTP_201_CREATED)
#         return Response(status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

# class EmailTokenObtainPairView(TokenObtainPairView):
#     serializer_class = TokenObtainPairSerializer
      
