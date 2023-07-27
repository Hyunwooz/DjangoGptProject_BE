from django.http import JsonResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile as PF_Model
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, LoginSerializer

User = get_user_model()

class Join(APIView):
    throttle_scope = 'contact'
    def post(self, request):
        serializer = UserSerializer(data=request.POST)

        if serializer.is_valid():
            user = serializer.save(request)
            profile = Profile.objects.create(user=user,avtarUrl='none')
            
            data = {
                'message': '회원가입을 축하합니다.'
            }
            
            return Response(data,status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors)


class Login(APIView):
    throttle_scope = 'contact'
    
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
            user_dict['password'] = "Secret"
            
            profile = PF_Model.objects.get(user=user)
            profile_dict = profile.__dict__
            profile_dict['_state'] = profile_dict['_state'].__dict__
            
            if profile_dict['avatarUrl'] != 'none':
                profile_dict['avatarUrl'] = 'http://127.0.0.1:8000/media/' + profile_dict['avatarUrl']
            
            data = {
                'user': {
                    'account': user_dict,
                    'profile': profile_dict
                    },
                'token': {
                        'access': access,
                        'refresh': refresh,
                    }
                }
            
            return Response(data=data,status=status.HTTP_200_OK)
        
        return JsonResponse(serializer.errors)
    

class Profile(APIView):
    throttle_scope = 'contact'
    
    def post(self, request):
        
        user = request.user
        profile = PF_Model.objects.get(user=user)
        name = request.POST['name']
        aboutMe = request.POST['aboutMe']
        
        try:
            avatarUrl = request.FILES['avatarUrl']
        except:
            profile.name = name
            profile.aboutMe = aboutMe
        else:
            profile.name = name
            profile.avatarUrl = avatarUrl
            profile.aboutMe = aboutMe
        
        profile.save()
        
        profile_dict = profile.__dict__
        profile_dict['_state'] = profile_dict['_state'].__dict__
      
        if profile_dict['avatarUrl'] != 'none':
            profile_dict['avatarUrl'] = 'http://127.0.0.1:8000/media/' + str(profile_dict['avatarUrl'])
        
        data = {
            "message": 'success',
            "profile": profile_dict
        }
        
        return JsonResponse(data)