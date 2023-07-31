from django.http import JsonResponse 
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .data import data as prompt
from .models import Answer
import json

# from .serializers import UserSerializer, LoginSerializer

User = get_user_model()

class Chat(APIView):
    def post(self, request):
        user = User.objects.get(email=request.user)
        req_data = json.loads(request.data)

        
        questions = {
            "role": "user",
            "content": request.data,
        }
        
        prompt.append(questions)
        
        ## conncet gpt api start
        response = requests.post('https://estsoft-openai-api.jejucodingcamp.workers.dev/', json=prompt)
        ai_anwser = response.json()['choices'][0]['message']['content']
        ## end
        
        remake = ai_anwser.replace("'",'"')
        gpt_anwser = json.loads(remake)

        answer = Answer.objects.create(
            writer=user,
            title=gpt_anwser["ad_title"],
            description=gpt_anwser["ad_description"],
            main_keyword=gpt_anwser["ad_Main_keyword"],
            recommand_keyword=gpt_anwser["ad_keyword"],
            category=gpt_anwser["ad_category"],
            type=gpt_anwser["ad_type"],
            question=req_data)
        
        answer_dict = answer.__dict__
        answer_dict['_state'] = ""
        
        data = {
                'message': answer_dict
            }
        
        return JsonResponse(data)


class LoungeChatList(APIView):
    def post(self, request):
        anwsers = list(Answer.objects.all().filter(is_active=True,is_public=True).order_by('-created_at').values())
        
        profile_add = []
        
        for ans in anwsers[:-1]:
            owner = User.objects.get(id=ans['writer_id'])
            owner_profile = owner.profile
            owner_dict = owner_profile.__dict__
            owner_dict['_state'] = ''
            ans['owner'] = owner_dict
            profile_add.append(ans)
            
        recents = anwsers[:3]
        
        datas = {
            "data": profile_add,
            "recents": recents
        }
        return JsonResponse(datas)


class MyChatList(APIView):
    def post(self, request):
        user = User.objects.get(email=request.user)
        anwsers = list(Answer.objects.filter(writer=user,is_active=True).order_by('-created_at').values())
        
        datas = {
            "data": anwsers
        }
        return JsonResponse(datas)
    

class ChatDetail(APIView):
    def post(self, request):
            
        anwser = Answer.objects.get(id=request.data)
        anwser.views = anwser.views + 1
        anwser.save()
        writer = anwser.writer
        profile = writer.profile
        
        r_answer = anwser.__dict__
        r_answer['_state'] = ''
        r_writer = writer.__dict__
        r_writer['_state'] = ''
        r_writer['password'] = 'sercret'
        r_profile = profile.__dict__
        r_profile['_state'] = ''
        
        datas = {
            "anwser": r_answer,
            "writer": r_writer,
            "profile": r_profile
        }
        return JsonResponse(datas)

class ChatDelete(APIView):
    def post(self, request):
        chat = Answer.objects.get(id=request.data)
        chat.is_active = False
        chat.save()
        
        datas = {
            "message": "삭제되었습니다.",
        }
        return JsonResponse(datas)
    

class ChatPublic(APIView):
    def post(self, request):
        chat = Answer.objects.get(id=request.data)
        chat.is_public = True
        chat.save()
        
        datas = {
            "message": "Public 설정 완료.",
        }
        return JsonResponse(datas)
    
    
class ChatPrivate(APIView):
    def post(self, request):
        chat = Answer.objects.get(id=request.data)
        chat.is_public = False
        chat.save()
        
        datas = {
            "message": "Private 설정 완료.",
        }
        return JsonResponse(datas)