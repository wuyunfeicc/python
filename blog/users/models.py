from django.db import models

# Create your models here.
class UserBiao(models.Model):
    usename = models.CharField(max_length=30)
    usepass = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    hobby = models.CharField(max_length=50)