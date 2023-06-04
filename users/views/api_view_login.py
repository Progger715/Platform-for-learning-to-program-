from rest_framework.views import APIView
from rest_framework.response import Response
from users.tools.user import User


class ApiViewLogin(APIView):

    def get(self, request):
        pass
        # return Response({'task': {task}, 'inner_data': {initial_code}, 'answer': {data_for_answer}})

    def post(self, request):
        login = request.data['login']
        password = request.data['password']
        # print(f"login ={login}")
        # print("password = ", password)
        result_checking = User.check_login(login, password)
        return Response({'result': result_checking})
