import random
import subprocess
from handler_code.collector_code import build_code_from_template
from handler_code.collector_code import get_html_result_compiling


def generate_loop_while_task():
    n = random.randint(5, 100)
    exercise = f"Вам дано число n = {n}.  Используя цикл while, вычислите сумму всех чисел от 1 до n. " \
               f"И выведите значение этой переменной с помощью команды System.out.println()"
    initial_code = f"int n = {n};\nint sum = 0;\n"
    return exercise, initial_code, n


# int sum = 0;
# int i = 1;
# while (i <= n) {
#    sum += i;
#    i++;
# }
# System.out.println(sum);
def check_correct_code_while(received_code: str, while_limit: int):
    message, flag_errors, out_compiling = get_html_result_compiling(received_code)
    if flag_errors:
        return message
    answer = sum(i for i in range(1, while_limit + 1))
    if str(answer) + "\n" == out_compiling:
        return ("Поздравляем, Вы успешно справились с заданием!")
    else:
        return ("К сожалению, Вы не справились с заданием! Проверьте свой код.")
