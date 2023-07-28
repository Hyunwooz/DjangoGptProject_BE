from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Question(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.JSONField(default=dict,blank=True) 
    views = models.IntegerField(default=0)
    like = models.JSONField(default=dict,blank=True)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.OneToOneField('Question',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    main_keyword = models.TextField()
    recommand_keyword = models.TextField()
    type = models.TextField()
    category = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    chat = models.ForeignKey(Question, on_delete=models.CASCADE) 
    content = models.CharField(max_length=30)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
