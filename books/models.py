from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 자동 증가하는 ID (기본 키)
    title = models.CharField(max_length=100)  # 문자열
    author = models.CharField(max_length=100)  # 문자열 
    price = models.IntegerField()  # 정수 필드
