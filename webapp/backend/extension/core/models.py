from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=400, verbose_name='Название', null=True)
    text = models.TextField(verbose_name='Текст', null=True)
    theme = models.CharField(max_length=400, verbose_name='Тема')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    summ = models.BooleanField(null=True, blank=True)
    ner = models.BooleanField(null=True, blank=True)
    ner_text = models.TextField(null=True, blank=True)
    parsing = models.BooleanField(null=True, blank=True)
    parsing_text = models.TextField(null=True, blank=True)
    percent = models.IntegerField(null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
