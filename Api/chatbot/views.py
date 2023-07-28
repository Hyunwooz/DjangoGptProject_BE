from django.http import JsonResponse 
from rest_framework.views import APIView
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
        
        prompt.append(req_data)
        ## conncet gpt api start
        ## end
        
        gpt_anwser = {
            "ad_title": "여자를 위한 제주도 자전거 여행",
            "ad_description": "아름다운 제주도의 자연을 만끽하며 자전거를 타는 특별한 경험을 느껴보세요. 친구, 가족, 연인과 함께 즐기는 잊지 못할 추억, 제주도의 다양한 문화와 역사를 배울 수 있는 기회입니다.",
            "ad_Main_keyword": "제주도 자전거 여행",
            "ad_keyword": "여행, 자전거 여행, 자전거 렌트",
            "ad_type": "검색",
            "ad_category": "여행",
        }
        
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
        anwsers = list(Answer.objects.filter(writer=user).order_by('-').values())
        
        datas = {
            "data": anwsers
        }
        return JsonResponse(datas)
