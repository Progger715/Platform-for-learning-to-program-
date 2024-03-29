from rest_framework.views import APIView
from rest_framework.response import Response

from handler_code.collector_code import get_html_result_compiling
from handler_code import helper_encryption
import handler_code.tasks_generators.generator_arithmetic_action as task_generation


class ApiViewAriphmeticTask(APIView):
    def __init__(self):
        self.true_answer = None
        # self.true_answer: str

    def get(self, request):
        task, initial_code, true_answer = task_generation.generate_math_expression_exercise()
        true_answer = helper_encryption.encrypt_data(str(true_answer))
        print("\nGET true_answer = ", true_answer)
        print("GET type(true_answer) = ", type(true_answer))
        return Response({'task': {task}, 'inner_data': {initial_code}, 'answer': {true_answer}})

    def post(self, request):
        received_code = request.data['code']
        received_answer = request.data['answer']
        received_answer = helper_encryption.decrypt_data(received_answer)
        print("received_answer = ", received_answer)
        print("type(received_answer) = ", type(received_answer))
        message, flag_errors, out_compiling = get_html_result_compiling(received_code)

        print("received_code =", message)
        print("flag_errors = ", flag_errors)
        print("\nout_compiling = ", out_compiling)
        print("type(out_compiling) = ", type(out_compiling))
        print("\nself.true_answer = ", self.true_answer)
        print("type(self.true_answer) = ", type(self.true_answer))

        if flag_errors:
            return Response({'result': message})
        else:
            if int(out_compiling) == int(received_answer):
                message = "Поздравляю, Вы справились с заданием верно!"
            else:
                message = f"Упс, Ваш ответ {out_compiling} не сходится с правильным. Проверьте свой код."
            return Response({'result': message})
