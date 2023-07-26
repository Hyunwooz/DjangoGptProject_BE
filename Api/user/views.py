from django.http import JsonResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer

User = get_user_model()

class Join(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.POST)

        if serializer.is_valid():
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
        
        return JsonResponse(serializer.errors)


class Login(APIView):

    def post(self, request):
        
        serializer = LoginSerializer(data={
            'email': request.POST["email"],
            'password': request.POST["password"]
        })
        
        if serializer.is_valid():
            
            user = serializer.validated_data['user']
            access = serializer.validated_data['access']
            refresh = serializer.validated_data['refresh']
            
            user_dict  = user.__dict__
            user_dict['_state'] = user_dict['_state'].__dict__
            
            data = {
                'user': user_dict,
                'access': access,
                'refresh': refresh,
                'is_login': True
            }
            return Response(data , status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors)