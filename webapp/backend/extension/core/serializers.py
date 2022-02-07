from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import Note
import requests
from .ner import ner
from .summarize import summarize
from .parsing.texts import execute

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'theme', 'user')


class NoteUserSerializer(ModelSerializer):
    summ = serializers.BooleanField(required=False, default=False)
    ner = serializers.BooleanField(required=False, default=False)
    ner_text = serializers.CharField(required=False)
    parsing = serializers.BooleanField(required=False, default=False)
    parsing_text = serializers.CharField(required=False)
    percent = serializers.IntegerField(required=False)
    text1 = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.theme = validated_data.get('theme', instance.theme)
        instance.text = validated_data.get('text', instance.text)
        instance.ner = validated_data.get('ner', instance.ner)
        instance.summ = validated_data.get('summ', instance.summ)
        instance.parsing = validated_data.get('parsing', instance.parsing)
        instance.text1 = validated_data.get('text1', instance.text1)

        if instance.ner:
            instance.ner_text = ner(instance.text1)
        if instance.parsing:
            instance.parsing_text = execute(instance.text1)
        if instance.summ:
            instance.text1 = summarize(instance.text1,
                                      validated_data.get('percent', instance.percent))

        instance.save()

        return instance

    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'theme', 'summ', 'ner', 'parsing', 'percent', 'text1',
                  'parsing_text', 'ner_text')


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token_access = serializers.CharField(required=False)
    token_refresh = serializers.CharField(required=False)
    email = serializers.EmailField()

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email", "token_access", "token_refresh")
