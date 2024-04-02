from rest_framework import serializers
from django.contrib.auth.models import User as AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AuthUser 
        fields = ['id', 'username', 'password', 'email']