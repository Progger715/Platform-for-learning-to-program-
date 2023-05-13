import random
import subprocess
from handler_code.collector_code import build_code_from_template

while_limit: int


def generate_loop_while_task():
    n = random.randint(5, 100)
    global while_limit
    while_limit = n
    exercise = f"Вам дано число n = {n} Используя цикл while, вычислите сумму всех чисел от 1 до n. " \
               f"И выведите значение этой переменной с помощью команды System.out.println()"
    initial_code = f"int n = {n};\nint sum = 0;\n"
    return exercise, initial_code


# int sum = 0;
# int i = 1;
# while (i <= n) {
#    sum += i;
#    i++;
# }
# System.out.println(sum);
def check_correct_code_while(received_code: str):
    path_to_file = build_code_from_template(received_code)
    result = subprocess.run(['java', path_to_file], capture_output=True, text=True)

    print(result)
    answer = sum(i for i in range(1, while_limit + 1))
    if str(answer) + "\n" == result.stdout:
        return ("Поздравляем, Вы успешно справились с заданием!")
    else:
        return ("К сожалению, Вы не справились с заданием! Проверьте свой код.")
