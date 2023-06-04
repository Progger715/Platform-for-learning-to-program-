import os

from rest_framework.views import APIView
from rest_framework.response import Response
from users.tools.user import User
from users.tools import my_cryptography


class ApiViewRegistration(APIView):

    def get(self, request):
        pass
        # return Response({'task': {task}, 'inner_data': {initial_code}, 'answer': {data_for_answer}})

    def post(self, request):
        firstName = request.data['firstName']
        lastName = request.data['lastName']
        middleName = request.data['middleName']
        email = request.data['email']
        password = request.data['password']
        print(locals())
        user = User()
        user.registrate_user(firstName, lastName, middleName, email, password)
        # salt = os.urandom(16)
        # firstName = my_cryptography.encrypt_data(request.data['firstName'])
        # lastName = my_cryptography.encrypt_data(request.data['lastName'])
        # middleName = my_cryptography.encrypt_data(request.data['middleName'])
        # email = my_cryptography.encrypt_data(request.data['email'])
        # password = my_cryptography.hash_data(request.data['password'], salt)
        # print(locals())
        # print(my_cryptography.decrypt_data(firstName))
        # print(my_cryptography.decrypt_data(lastName))
        # print(my_cryptography.decrypt_data(middleName))
        # print(my_cryptography.decrypt_data(email))
        # new_password = my_cryptography.hash_data('password', salt)
        # if new_password == password:
        #     print("equal")
        # else:
        #     print("not equal")
        # print(locals())

        return Response({'result': 'true'})
