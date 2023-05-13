import subprocess
from handler_code.collector_code import build_code_from_template


def generate_condition_task():
    exercise = f"Напишите программу на Java, которая определяет, является ли введенное пользователем" \
               f" число четным или нечетным.\nПроверьте переменную number на четность и выведите соответвующий овтет " \
               f'"четно" или "нечетно" в консоль с помощью команды System.out.println().'

    initial_code = "Scanner scanner = new Scanner(System.in);\n" \
                   "int number = scanner.nextInt();\n"
    return exercise, initial_code


# if(number % 2 == 0) {
# System.out.println("четно");
# }
# else {
# System.out.println("нечетно");
# }
def check_correct_code(received_code: str):
    # создаем временный файл для последующего запуска
    path_to_file = build_code_from_template(received_code)

    check_values = [1, 2, 0, -1, -2, 100, -100, 1111111111]
    for value in check_values:
        result = subprocess.run(['java', path_to_file], input=str(value), capture_output=True, text=True)
        if result.stderr != "":
            return "Ошибка компиляции! Проверьте свой код."
        if value % 2 != 0 and result.stdout == "четно\n":
            return "проверка не пройдена на числе = ", value
        if value % 2 == 0 and result.stdout == "нечетно\n":
            return "проверка не пройдена на числе = ", value
    return "Поздравляем, Вы успешно справились с заданием!!"
