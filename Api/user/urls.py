from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from .views import Join, Login

app_name = 'user'

urlpatterns = [
    path("join/", Join.as_view(), name='join'),
    path("login/", Login.as_view(), name="login"),
    
    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # path("logout/", Logout.as_view(), name='logout'),
    # path("changePassword/", ChangePassWord.as_view(), name='change-pw'),
    # path("profile/edit/", ProfileUpdate.as_view(), name='pf-edit'),
] 

