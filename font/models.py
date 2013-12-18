from django.db import models


class Fonts(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=100)
    decs = models.CharField(max_length=1000)


class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    fonts = models.ManyToManyField(Fonts)