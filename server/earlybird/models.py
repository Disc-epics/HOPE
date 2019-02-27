from django.db import models


class User(models.Model):
    name = models.CharField()
    email = models.CharField()


class Client(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    middle_name = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
