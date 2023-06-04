from django.db import models


class UsersLogin(models.Model):
    firstName = models.BinaryField()
    lastName = models.BinaryField()
    middleName = models.BinaryField()
    login = models.CharField(max_length=35, unique=True)
    password = models.BinaryField()
    salt = models.BinaryField()
    role = models.CharField(max_length=35)
    date_registration = models.DateTimeField()

    def __str__(self):
        return self.login
