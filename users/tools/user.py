import os
from datetime import datetime
from users.tools import my_cryptography
from users.models import UsersLogin


class User:
    def registrate_user(self, first_name, last_name, middle_name, email, password):
        salt = os.urandom(16)
        date = datetime.now()
        first_name = my_cryptography.encrypt_data(first_name)
        last_name = my_cryptography.encrypt_data(last_name)
        middle_name = my_cryptography.encrypt_data(middle_name)
        email = my_cryptography.encrypt_data(email)
        password = my_cryptography.hash_data(password, salt)

        UsersLogin.objects.create(firstName=first_name,
                                  lastName=last_name,
                                  middleName=middle_name,
                                  login=email,
                                  password=password,
                                  salt=salt,
                                  date_registration=date,
                                  role="student")
