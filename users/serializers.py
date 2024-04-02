from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User 
        fields = ('id', 'fullname', 'password','email', 'role', 'refreshToken', 'createdDate')
        extra_kwargs = {'password': {'write_only': True}}