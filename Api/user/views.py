from django.http import JsonResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

class Join(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.POST)

        if serializer.is_valid(raise_exception=False):
            user = serializer.save(request)

            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)
            
            data = {
                'user': user,
                'access': access,
                'refresh': refresh 
            }
            print(data)
            return Response(data=data,status=status.HTTP_201_CREATED)
        

class Login(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.POST)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            access = serializer.validated_data['access']
            refresh = serializer.validated_data['refresh']
            
            data = {
                'user': user,
                'access': access,
                'refresh': refresh 
            }
            return Response(data=data,status=status.HTTP_200_OK)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)