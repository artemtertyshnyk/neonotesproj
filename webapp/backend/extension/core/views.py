from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *


class NoteUserList(generics.ListCreateAPIView):
    serializer_class = NoteUserSerializer

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        data = request.data
        note = Note.objects.create(title=data['title'], text=data['text'], theme=data['theme'], user=self.request.user)
        note.save()

        serializer = NoteUserSerializer(note)

        return Response(serializer.data)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteUserSerializer

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        user = UserModel.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email'],
        )
        response = requests.post('http://localhost:8000/api/v1/token/',
                                 {'username': data['username'],
                                  'password': data['password']})
        data1 = {'id': user.id, 'username': data['username'], 'password': data['password'], 'email': data['email'],
                 'token_access': response.json()['access'], 'token_refresh': response.json()['refresh']}
        serializer = UserSerializer(data1)

        return Response(serializer.data)
