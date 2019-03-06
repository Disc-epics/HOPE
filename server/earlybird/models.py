from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
