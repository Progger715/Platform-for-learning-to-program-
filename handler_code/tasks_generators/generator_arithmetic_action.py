import random


def generate_math_expression_exercise():
    def calculate_expression_result(a, b, c, operators):
        result = a
        for operator in operators:
            if operator == '+':
                result += b
            elif operator == '-':
                result -= b
            elif operator == '*':
                result *= b
            # else:
            #     result /= b
            b = c  # Применяем следующее число к следующей операции (если есть)
        return result

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    # Сгенерируйте случайные операторы из списка доступных операторов
    operators = ['+', '-', '*']
    num_operators = random.randint(2, 3)
    # print("num_operators = ", num_operators)
    selected_operators = random.sample(operators, num_operators)
    # print("selected_operators = ", selected_operators)

    # Вычислите ожидаемый ответ в зависимости от операторов
    answer = calculate_expression_result(a, b, c, selected_operators)

    # Сформулируйте задание для пользователя
    operator_symbols = ' '.join(selected_operators)
    exercise = f"Даны три числа: {a}, {b} и {c}. Выполните математические операции '{operator_symbols}' " \
               f"между ними и получите ответ {answer}. Выведите ответ на экран (команда System.out.println())."

    initial_code = create_initial_code_for_user((a, b, c))

    return exercise, initial_code, answer


def create_initial_code_for_user(inner_data: tuple):
    variables = ["a", "b", "c"]
    template_string = "int %s = %s;"
    result = f""
    for i in range(3):
        result += template_string % (variables[i], inner_data[i]) + "\n"
    return result


# task, inner_data, answer = generate_math_expression_exercise()
print(generate_math_expression_exercise())
