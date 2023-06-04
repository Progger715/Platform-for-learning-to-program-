from django.db import models


class UsersLogin(models.Model):
    firstName = models.BinaryField(
        default=b'gAAAAABke4b4PW_j5Vx7QIgMNMfs1lrszvSr_VYVjB4Ccx7OGM9xGXFKf3T0CJmgu7AP2viRhUW0p4CQu66b0lQrFXb2lY7UVA==')
    lastName = models.BinaryField(
        default=b'gAAAAABke4b4PW_j5Vx7QIgMNMfs1lrszvSr_VYVjB4Ccx7OGM9xGXFKf3T0CJmgu7AP2viRhUW0p4CQu66b0lQrFXb2lY7UVA=='
    )
    middleName = models.BinaryField(
        default=b'gAAAAABke4b4PW_j5Vx7QIgMNMfs1lrszvSr_VYVjB4Ccx7OGM9xGXFKf3T0CJmgu7AP2viRhUW0p4CQu66b0lQrFXb2lY7UVA=='
    )
    login = models.BinaryField(unique=True)
    password = models.BinaryField()
    salt = models.BinaryField()
    role = models.CharField(max_length=35)
    date_registration = models.DateTimeField()

    def __str__(self):
        return self.login
