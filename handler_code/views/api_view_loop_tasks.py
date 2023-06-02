from rest_framework.views import APIView
from rest_framework.response import Response

import handler_code.tasks_generators.generator_loop_tasks as task_generation
from handler_code import helper_encryption


class ApiViewLoopTask(APIView):

    def get(self, request):
        task, initial_code, data_for_answer = task_generation.generate_loop_while_task()
        data_for_answer = helper_encryption.encrypt_data(str(data_for_answer))
        return Response({'task': {task}, 'inner_data': {initial_code}, 'answer': {data_for_answer}})

    def post(self, request):
        received_code = request.data['code']
        data_for_answer = request.data['answer']
        print("data_for_answer = ", data_for_answer)
        print("type(data_for_answer) = ", type(data_for_answer))
        data_for_answer = int(helper_encryption.decrypt_data(data_for_answer))
        print("\nafter decryption")
        print("data_for_answer = ", data_for_answer)
        print("type(data_for_answer) = ", type(data_for_answer))
        message = task_generation.check_correct_code_while(received_code, data_for_answer)

        return Response({'result': message})
