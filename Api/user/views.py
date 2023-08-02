from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse 
from django.contrib.auth import get_user_model
from .models import Profile as PF_Model
from .serializers import UserSerializer, LoginSerializer, GithibLoginSerializer
import requests

User = get_user_model()

CLIENT_ID = '3a029223a08dd902d643'
CLIENT_SECRET = '47db3bedb554bbf7d9e7a55167be6acb33c416e3'
redirect_uri = "http://127.0.0.1:5500/src/view/login.html"

class GithubLogin(APIView):
    def post(self, request):
        
        data = {
            'url': f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={redirect_uri}"
        }
        return JsonResponse(data)


class GithubLogin_callback(APIView):
    def post(self, request):
        code = request.data['code']
        token_req = requests.post(
        f"https://github.com/login/oauth/access_token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={code}&accept=&json&redirect_uri={redirect_uri}&response_type=code", headers={'Accept': 'application/json'})
        
        token_req_json = token_req.json()
        error = token_req_json.get("error")
        access_token = token_req_json.get('access_token')
        user_req = requests.get(f"https://api.github.com/user",headers={"Authorization": f"Bearer {access_token}"})
        user_json = user_req.json()
        
        #  '@github.com'
        
        # email = user_json.get("login")
        name = user_json.get("name")
        login = user_json.get("login")
        email = login + '@github.com'
        avatar_url = user_json.get("avatar_url")
        
        try:
            user_check = User.objects.get(email=email)
        except:
            user_check = User.objects.create(
                email=email,
                login_method='github',
            )
            profile = PF_Model.objects.create(user=user_check,avatarUrl=avatar_url,name=name)
            
        serializer = GithibLoginSerializer(data={
            'email': email,
        })

        if serializer.is_valid():
            user = serializer.validated_data['user']
            access = serializer.validated_data['access']
            refresh = serializer.validated_data['refresh']

            user_dict  = user.__dict__
            user_dict['_state'] = user_dict['_state'].__dict__

            profile = PF_Model.objects.get(user=user)
            profile_dict = profile.__dict__
            profile_dict['_state'] = profile_dict['_state'].__dict__

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

class Join(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.POST)

        if serializer.is_valid():
            user = serializer.save(request)
            profile = PF_Model.objects.create(user=user,avatarUrl='none')
            
            data = {
                'message': '회원가입을 축하합니다.'
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