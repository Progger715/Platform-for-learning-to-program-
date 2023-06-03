from django.db import models


class UsersLogin(models.Model):
    login = models.CharField(max_length=35, unique=True)
    password = models.BinaryField()
    salt = models.BinaryField()
    role = models.CharField(max_length=35)
    date_registration = models.DateTimeField()

