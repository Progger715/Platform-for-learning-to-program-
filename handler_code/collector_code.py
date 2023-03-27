import subprocess
import jinja2
import openai

from lms_programming.config import config


def build_code_from_template(users_code: str):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(
        "/home/bogdan/study/lms_project/Platform-for-learning-to-program-/handler_code/java_code/templates_java_code"))  # "java_code/templates_java_code/"))
    template = environment.get_template("MainTemplate.java")
    content = template.render(data=users_code)
    # print(content)
    name_file = "/home/bogdan/study/lms_project/Platform-for-learning-to-program-/handler_code/java_code/final_code/Main.java"
    with open(name_file, mode="w", encoding="utf-8") as file_for_save:
        file_for_save.write(content)
    return name_file


def run_code(path_to_java_file: str):
    try:
        result = subprocess.run(['java', path_to_java_file], capture_output=True)
        print("result compiling\n", result)
        if len(result.stderr.decode()) == 0:
            response_server = f"Поздравляем!\nКомпиляция прошла успешна!\n{result.stdout.decode()}"
            flag_errors = False
            line_error = None
        else:

            message_error = __short_message_error(result.stderr.decode())
            translate = __get_data_about_error(message_error)

            response_server = f"Упс! возникли следующие ошибки:\n{message_error}\n\nперевод:{translate}"
            flag_errors = True
            line_error = __get_line_with_error(message_error)
        return response_server, flag_errors, line_error
    except Exception as ex:
        print("[ERROR] compile_code\n", ex)


def get_html_result_compiling(user_code: str):
    return run_code(build_code_from_template(user_code))


def __get_data_about_error(error: str):
    import time
    openai.api_key = config.OPENAI_API_KEY
    prompt_ru = f"дай перевод ошибки в java: {error} Только перевод, не нужно пояснять."
    prompt_ru_answer = f"скажи кратко, как решаить следующую ошибку в java: {error}"
    prompt_en = f"give translation of the error in java into Russian: {error} Only translation, no need to explain."

    start_time = time.time_ns()
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt_en, max_tokens=100)
    end_time = time.time_ns()
    delta_en = end_time - start_time
    print("time en=", delta_en)
    # print("english answer:\n", response.choices[0].text, "\n")

    # start_time = time.time_ns()
    # response = openai.Completion.create(engine="text-davinci-003", prompt=prompt_ru, max_tokens=300)
    # end_time = time.time_ns()
    # delta_ru = end_time - start_time
    # print("time ru=", delta_ru)
    # print("russian answer:\n", response.choices[0].text)
    # print(f"time_ru <= time_en: {delta_ru <= delta_en}\ndelta = {delta_ru - delta_en}")
    return response.choices[0].text


def __short_message_error(errors: str):
    start_index = errors.find(".java:") + 9
    return errors[start_index:]


def __get_line_with_error(message_error: str):
    start_index = message_error.find("\n")
    end_index = message_error.find("\n", start_index + 1)
    return message_error[start_index:end_index]


if __name__ == '__main__':
    data = """System.out.println("Hello, world!")"""
    # name_file = "java_code/final_code/Main.java"
    # build_code_from_template(stroka)
    # print(compile_code(name_file))
    print(get_html_result_compiling(data))
