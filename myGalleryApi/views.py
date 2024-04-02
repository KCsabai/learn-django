from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as AuthUser
from users.models import User
from rest_framework.authtoken.models import Token

from .serializers import AuthUserSerializer
from users.serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    request.data['username'] = request.data['email'].split('@')[0]
    auth_serializer = AuthUserSerializer(data=request.data)
    serializer = UserSerializer(data=request.data)
    if auth_serializer.is_valid() and serializer.is_valid():
        auth_serializer.save()
        auth_user = AuthUser.objects.get(email=request.data['email'])
        auth_user.set_password(request.data['password'])
        auth_user.save()
        token = Token.objects.create(user=auth_user)

        serializer.save()
        user = AuthUser.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()

        return Response({'tokens': { 'accessToken': token.key }, 'user': auth_serializer.data})
    return Response(auth_serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(AuthUser, email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = AuthUserSerializer(user)
    return Response({'tokens': { 'accessToken': token.key }, 'user': serializer.data})
