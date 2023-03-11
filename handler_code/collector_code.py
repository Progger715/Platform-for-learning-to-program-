import subprocess
import jinja2


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
        # print("res =\n", result)
        if len(result.stderr.decode()) == 0:
            response_server = f"Поздравляем!\nКомпиляция прошла успешна!\n{result.stdout.decode()}"
        else:
            response_server = f"Упс! возникли следующие ошибки:\n{result.stderr.decode()}"
        return response_server
    except Exception as ex:
        print("[ERROR] compile_code\n", ex)


def get_html_result_compiling(user_code: str):
    return run_code(build_code_from_template(user_code))


if __name__ == '__main__':
    data = """System.out.println("Hello, world!")"""
    # name_file = "java_code/final_code/Main.java"
    # build_code_from_template(stroka)
    # print(compile_code(name_file))
    print(get_html_result_compiling(data))
