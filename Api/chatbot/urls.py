from django.urls import path
from .views import Chat, MyChatList, ChatDetail, ChatDelete, ChatPublic, ChatPrivate, LoungeChatList, CommentWrite, CommentDelete, Search, Like

app_name = 'chatbot'

urlpatterns = [
    path("", Chat.as_view(), name='main'),
    path("mylist/", MyChatList.as_view(), name='mylist'),
    path("lounge/", LoungeChatList.as_view(), name='lounge'),
    path("detail/", ChatDetail.as_view(), name='detail'),
    path("delete/", ChatDelete.as_view(), name='delete'),
    path("public/", ChatPublic.as_view(), name='public'),
    path("private/", ChatPrivate.as_view(), name='private'),
    path("comment/write/", CommentWrite.as_view(), name='cm-write'),
    path("comment/delete/", CommentDelete.as_view(), name='cm-delete'),
    path("search/", Search.as_view(), name='search'),
    path("like/", Like.as_view(), name='like'),
] 

