from django.db import models
import datetime


class Fonts(models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=100)
    decs = models.CharField(max_length=1000)


class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    fonts = models.ManyToManyField(Fonts)
    register_time = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(default=datetime.datetime(1949,1,1))

    # status
    sid = models.IntegerField(max_length=20, blank=True, null=True)