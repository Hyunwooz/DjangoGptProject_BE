from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse 
from django.contrib.auth import get_user_model
from django.db.models import Count
from .data import data as prompt
from .models import Answer, Comment
import requests
import json

User = get_user_model()


class Chat(APIView):
    throttle_scope = 'chatbot'
    permission_classes = [IsAuthenticated,]
    
    def post(self, request):
        
        user = request.user
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
        
        data = {
                'message': 'Success'
            }
        
        return JsonResponse(data)


class LoungeChatList(APIView):
    def post(self, request):
        anwsers = list(Answer.objects.all().filter(is_active=True,is_public=True).order_by('created_at').values())
        categories = list(Answer.objects.filter(is_active=True,is_public=True).values('category').annotate(count=Count('category')))
        
        profile_add = []
        
        for ans in anwsers:
            owner = User.objects.get(id=ans['writer_id'])
            owner_profile = owner.profile
            owner_dict = owner_profile.__dict__
            owner_dict['_state'] = ''
            ans['owner'] = owner_dict
            profile_add.append(ans)
            
        recents = anwsers[:3]
        
        datas = {
            "data": profile_add,
            "recents": recents,
            "categories": categories
        }
        return JsonResponse(datas)


class MyChatList(APIView):
    permission_classes = [IsAuthenticated,]
    
    def post(self, request):
        user = request.user
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
        
        comments = list(Comment.objects.filter(chat=anwser,is_active=True).values())
        r_comments = []
        
        for comment in comments:
            owner = User.objects.get(id=comment['writer_id'])
            owner_profile = owner.profile
            owner_dict = owner_profile.__dict__
            owner_dict['_state'] = ''
            comment['owner'] = owner_dict
            r_comments.append(comment)
        
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
            "profile": r_profile,
            "comments": r_comments
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


class CommentWrite(APIView):
    permission_classes = [IsAuthenticated,]
    
    def post(self, request):
        user = request.user
        chat = Answer.objects.get(id=request.data['post_id'])
        comment = Comment.objects.create(writer=user,content=request.data['comment'],chat=chat)
        
        datas = {
            "message": "댓글 생성 완료",
        }
        return JsonResponse(datas)


class CommentDelete(APIView):
    def post(self, request):
        comment = Comment.objects.get(id=request.data)
        comment.is_active = False
        comment.save()
        
        datas = {
            "message": "삭제되었습니다.",
        }
        return JsonResponse(datas)


class Search(APIView):
    def post(self, request):
        
        if request.data['type'] == 'category':
            anwsers = list(Answer.objects.all().filter(category=request.data['search'],is_active=True,is_public=True).order_by('created_at').values())
        elif request.data['type'] == 'title':
            anwsers = list(Answer.objects.all().filter(title__contains=request.data['search'],is_active=True,is_public=True).order_by('created_at').values())

        categories = list(Answer.objects.filter(is_active=True,is_public=True).values('category').annotate(count=Count('category')))
        
        profile_add = []
        
        for ans in anwsers:
            owner = User.objects.get(id=ans['writer_id'])
            owner_profile = owner.profile
            owner_dict = owner_profile.__dict__
            owner_dict['_state'] = ''
            ans['owner'] = owner_dict
            profile_add.append(ans)
            
        recents = anwsers[:3]
        
        datas = {
            "data": profile_add,
            "recents": recents,
            "categories": categories
        }
        return JsonResponse(datas)


class Like(APIView):
    
    def post(self, request):

        chat = Answer.objects.get(id=request.data)
        user = request.user.email
        
        try:
            chat.like[user]
        except:
            chat.like[user] = 'like'
        else:
            if   chat.like[user] == 'like':
                chat.like[user] = 'unlike'
            else:
                chat.like[user] = 'like'
        
        chat.save()
        
        data = {
            'message': 'success'
        }
        return JsonResponse(data)
