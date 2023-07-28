from django.contrib import admin
from .models import Answer,Question,Comment

# Register your models here.
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Comment)