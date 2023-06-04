import os
from datetime import datetime
from users.tools import my_cryptography
from users.models import UsersLogin


class User:
    @staticmethod
    def registrate_user(first_name: str, last_name: str, middle_name: str, login: str, password: str):
        salt = os.urandom(16)
        date = datetime.now()
        first_name = my_cryptography.encrypt_data(first_name)
        last_name = my_cryptography.encrypt_data(last_name)
        middle_name = my_cryptography.encrypt_data(middle_name)
        password = my_cryptography.hash_data(password, salt)

        UsersLogin.objects.create(firstName=first_name,
                                  lastName=last_name,
                                  middleName=middle_name,
                                  login=login,
                                  password=password,
                                  salt=salt,
                                  date_registration=date,
                                  role="student")

    @staticmethod
    def check_login(login: str, password: str):
        user = UsersLogin.objects.get(login=login)
        try:
            password = my_cryptography.hash_data(password, bytes(user.salt))
            if password == user.password:
                # print("PASSWORD EQUAL!")
                return True
            else:
                # print("PASSWORD NOT EQUAL!")
                return False
        except Exception as ex:
            print(ex)
            return False

        # login = my_cryptography.encrypt_data(login)
        # old_login = b'gAAAAABkfGnp8LPxiZqZvB5Q61w0k_drzLa8YwrX4Fho86kjFZn0edAzmym0Cl5DOZ0yQzUyfbdmNEH5uf4KfJxhZeNQ_3TB7g=='
        # print("old_login = ", old_login)
        # print("my_login = ", login)
        # print("decrypt my_login = ", my_cryptography.decrypt_data(login))
        # print("type(my_login) = ", type(login))
        # my_salt = os.urandom(16)
        # print("my_salt = ", my_salt)
        # # print("type(my_salt) = ", type(my_salt))
        # login = b'gAAAAABkfFReD3p6bmKkmBWw2g9_LcGurDcRVWmFSORY391XKLKsGQ2Vx-xkswyJTTHOOp9tLUv2C0_nlc4g-YKpliUCBhdDtw=='
        # print("login crypt = ", login)
        # # тут надо получить все данные пользователя с указанным логином
        # user = UsersLogin.objects.get(login=login)
        # print("user.login = ", user.login)
        # print("user.firstName = ", user.firstName)
        # print("user.lastName = ", user.lastName)
        # print("user.middleName = ", user.middleName)
        # print("user.date_registration = ", user.date_registration)
        # # print("\nuser.salt = ", user.salt)
        # # print("user.salt.hex() = ", user.salt.hex())
        # # print("type(user.salt) = ", type(user.salt))
        # # print("\nuser.password = ", user.password)
        # # print("user.password.hex = ", user.password.hex())
        # # print("type(user.password) = ", type(user.password))
        # password = my_cryptography.hash_data(password, bytes(user.salt))
        # # print("\nmy_password = ", password)
        # # print("type(my_password) = ", type(password))
        # decrypt_login = my_cryptography.decrypt_data(user.login)
        # print("\ndecrypt_login = ", decrypt_login)
        # if password == user.password:
        #     print("PASSWORD EQUAL!")
        # else:
        #     print("PASSWORD NOT EQUAL!")
