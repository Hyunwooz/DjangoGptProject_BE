from django.http import JsonResponse 
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .data import data as prompt
from .models import Question, Answer
import json

# from .serializers import UserSerializer, LoginSerializer

User = get_user_model()

class Chat(APIView):
    def post(self, request):
        user = User.objects.get(email=request.user)
        req_data = json.loads(request.data)
        question = Question.objects.create(writer=user,content=req_data)
        
        questions = {
            "role": "user",
            "content": request.data,
        }
        
        prompt.append(questions)
        ## conncet gpt api start
        response = requests.post('https://estsoft-openai-api.jejucodingcamp.workers.dev/', json=prompt)
        anwser = response.json()['choices'][0]['message']['content']
        ## end
        remake = anwser.replace("'",'"')
        gpt_anwser = json.loads(remake)
        
        anwser = Answer.objects.create(
            question=question,
            writer=user,
            title=gpt_anwser["ad_title"],
            description=gpt_anwser["ad_description"],
            main_keyword=gpt_anwser["ad_Main_keyword"],
            recommand_keyword=gpt_anwser["ad_keyword"],
            type=gpt_anwser["ad_type"],
            category=gpt_anwser["ad_category"]
            )
        
        answer_dict = anwser.__dict__
        answer_dict['_state'] = ""
        
        data = {
                'message': answer_dict
            }
        
        return JsonResponse(data)
    

class MyChatList(APIView):
    def post(self, request):
        user = User.objects.get(email=request.user)
        anwsers = list(Answer.objects.filter(writer=user).order_by('-created_at').values())
        
        datas = {
            "data": anwsers
        }
        return JsonResponse(datas)
    

class ChatDetail(APIView):
    def post(self, request):
            
        anwser = Answer.objects.get(id=request.data)
        qeustion = anwser.question
        writer = anwser.writer
        profile = writer.profile
        
        r_answer = anwser.__dict__
        r_answer['_state'] = ''
        r_qeustion = qeustion.__dict__
        r_qeustion['_state'] = ''
        r_writer = writer.__dict__
        r_writer['_state'] = ''
        r_writer['password'] = 'sercret'
        r_profile = profile.__dict__
        r_profile['_state'] = ''
        
        datas = {
            "anwser": r_answer,
            "qeustion": r_qeustion,
            "writer": r_writer,
            "profile": r_profile
        }
        return JsonResponse(datas)
