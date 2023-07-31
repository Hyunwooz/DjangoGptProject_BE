from django.urls import path
from .views import Chat, MyChatList, ChatDetail

app_name = 'chatbot'

urlpatterns = [
    path("", Chat.as_view(), name='main'),
    path("mylist/", MyChatList.as_view(), name='mylist'),
    path("lounge/", MyChatList.as_view(), name='lounge'),
    path("detail/", ChatDetail.as_view(), name='detail'),
] 

