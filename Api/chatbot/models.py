from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Answer(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.JSONField(default=dict,blank=True) 
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    main_keyword = models.CharField(max_length=200,null=True,blank=True)
    recommand_keyword = models.CharField(max_length=200,null=True,blank=True)
    type = models.CharField(max_length=200,null=True,blank=True)
    category = models.CharField(max_length=200,null=True,blank=True)
    views = models.IntegerField(default=0)
    like = models.JSONField(default=dict,blank=True)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    chat = models.ForeignKey(Answer, on_delete=models.CASCADE) 
    content = models.CharField(max_length=30)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
