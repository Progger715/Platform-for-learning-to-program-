from rest_framework.views import APIView
from rest_framework.response import Response


class ApiViewLogin(APIView):

    def get(self, request):
        pass
        # return Response({'task': {task}, 'inner_data': {initial_code}, 'answer': {data_for_answer}})

    def post(self, request):
        return Response({'result': 'false'})
