from django.http import JsonResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer
# from .forms import LoginForm

User = get_user_model()

class Join(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.POST)

        if serializer.is_valid(raise_exception=False):
            user = serializer.save(request)

            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)
            
            user_dict  = user.__dict__
            user_dict['_state'] = user_dict['_state'].__dict__
            
            data = {
                'user': user_dict,
                'access': access,
                'refresh': refresh 
            }
            
            return Response(data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        
        # print(serializer.validate(data=request.POST))
        
        if serializer.validate(data=request.POST):
            
            passData = serializer.validate(data=request.POST)
            
            user = passData['user']
            access = passData['access']
            refresh = passData['refresh']
            
            user_dict  = user.__dict__
            user_dict['_state'] = user_dict['_state'].__dict__
            
            data = {
                'user': user_dict,
                'access': access,
                'refresh': refresh
            }
            
            return Response(data , status=status.HTTP_200_OK)
        
        return Response(serializer.error_messages , status=status.HTTP_400_BAD_REQUEST)