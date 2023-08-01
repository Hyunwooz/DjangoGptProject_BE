from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ['email', 'password']

    def save(self, request):
        user = super().save()

        user.email = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)
    
    def validate(self, data):
        
        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, password=password)
        
        if user:
            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)

            data = {
                'user': user,
                'refresh': refresh,
                'access': access,
            }

            return data
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise serializers.ValidationError("비밀번호가 틀렸습니다.")
        else:
            raise serializers.ValidationError("존재하지 않는 이메일 입니다.")
        
        raise serializers.ValidationError('이메일 또는 비밀번호를 확인해주세요.')
            

class GithibLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    
    def validate(self, data):
        
        email = data.get('email', None)
        user = User.objects.get(email=email)
        
        if user:
            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)

            data = {
                'user': user,
                'refresh': refresh,
                'access': access,
            }

            return data
        
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
        else:
            raise serializers.ValidationError("존재하지 않는 이메일 입니다.")
        raise serializers.ValidationError('이메일 또는 비밀번호를 확인해주세요.')