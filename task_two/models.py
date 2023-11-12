import uuid

from django.db import models


class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    home_city = models.CharField(max_length=100)
