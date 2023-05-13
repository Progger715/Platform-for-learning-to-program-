from rest_framework.views import APIView
from rest_framework.response import Response

import handler_code.tasks_generators.generator_loop_tasks as task_generation


class ApiViewLoopTask(APIView):

    def get(self, request):
        task, initial_code = task_generation.generate_loop_while_task()
        return Response({'task': {task}, 'inner_data': {initial_code}})

    def post(self, request):
        received_code = request.data['code']
        message = task_generation.check_correct_code_while(received_code)

        return Response({'result': message})
