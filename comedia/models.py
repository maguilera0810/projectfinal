from django.db import models

# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=604, null=False)
    url = models.CharField(max_length=100, null=False)
    tipo = models.CharField(max_length=100, null=False)


class Client(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64, unique=True)
    email = models.EmailField()


class Comment(models.Model):
    user_id = models.CharField(null=False, max_length=60)
    rank = models.IntegerField(null=False)
    comment = models.CharField(null=True, max_length=300)
