from rest_framework.views import APIView
from rest_framework.response import Response

from handler_code.collector_code import get_html_result_compiling


class HandlerCodeApiView(APIView):
    def get(self, request):
        return Response({'title': 'Template'})

    def post(self, request):
        print("request = ", request)
        received_code = request.data['code']
        print("request.received_code = ", received_code)
        print("type(received_code) = ", type(received_code))
        received_code, flag_errors, line_error = get_html_result_compiling(received_code)
        print("received_code", received_code)
        print("flag_errors", flag_errors)
        print("line_error", line_error)
        return Response({'result': received_code})
