from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse 
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, reverse
from .models import Profile as PF_Model
from .serializers import UserSerializer, LoginSerializer, GithibLoginSerializer
import requests

User = get_user_model()

class GithubLogin(APIView):
    def post(self, request):
        
        # client_id = os.environ.get("GH_ID")
        client_id = "3a029223a08dd902d643"
        redirect_uri = "http://127.0.0.1:8000/user/login/github/callback/"
        scope = "read:user"
        return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}")


class GithubLogin_callback(APIView):
    def post(self, request):

        code = request.GET.get("code", None)
        client_id = "3a029223a08dd902d643"
        client_secret = '47db3bedb554bbf7d9e7a55167be6acb33c416e3'

        token_request = requests.post(
            f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
            headers={"Accept": "application/json"},
        )
        token_json = token_request.json()
        # error = token_json.get("error", None)
        access_token = token_json.get("access_token")
        profile_request = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"token {access_token}",
                "Accept": "application/json",
            },
        )
        profile_json = profile_request.json()
        avatar_url = profile_json.get("avatar_url", None)
        name = profile_json.get("name", None)
        email = profile_json.get("email", None)
        
        try:
            user = User.objects.get(email=email)
        except:
            user = User.objects.create(
                email=email,
                login_method='github',
            )
            
            profile = PF_Model.objects.create(user=user,avatarUrl=avatar_url,name=name)
        else:
            user = User.objects.get(email=email)


        serializer = GithibLoginSerializer(data={
            'email': email,
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
    

class Join(APIView):
    throttle_scope = 'contact'
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