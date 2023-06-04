from rest_framework.views import APIView
from rest_framework.response import Response
from users.tools.user import User


class ApiViewRegistration(APIView):

    def get(self, request):
        pass

    def post(self, request):
        firstName = request.data['firstName']
        lastName = request.data['lastName']
        middleName = request.data['middleName']
        email = request.data['email']
        password = request.data['password']
        print(locals())
        user = User()
        user.registrate_user(firstName, lastName, middleName, email, password)

        return Response({'result': 'true'})
