from rest_framework.views import APIView
from rest_framework.response import Response

import handler_code.tasks_generators.generator_condition_tasks as task_generation


class ApiViewConditionTask(APIView):

    def get(self, request):
        task, initial_code = task_generation.generate_condition_task()
        return Response({'task': {task}, 'inner_data': {initial_code}})

    def post(self, request):
        received_code = request.data['code']
        result_test = task_generation.check_correct_code(received_code)
        return Response({'result': result_test})
