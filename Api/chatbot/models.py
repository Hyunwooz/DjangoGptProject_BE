from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class ChatHistory(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='blog/media',null=True,blank=True)
    views = models.IntegerField(default=0)
    like = models.JSONField(default={},null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    ChatHistory = models.ForeignKey(ChatHistory, on_delete=models.CASCADE) 
    content = models.CharField(max_length=30)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Comment on {self.post.title}'