from rest_framework import serializers
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

    def validate(self, data):
        email = data.get('email', None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("user already exists")

        return data