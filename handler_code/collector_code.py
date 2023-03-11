import subprocess
import jinja2


def build_code_from_template(users_code: str):
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader("/home/bogdan/study/lms_project/Platform-for-learning-to-program-/handler_code/java_code/templates_java_code"))#"java_code/templates_java_code/"))
    template = environment.get_template("MainTemplate.java")
    content = template.render(data=users_code)
    # print(content)
    name_file = "/home/bogdan/study/lms_project/Platform-for-learning-to-program-/handler_code/java_code/final_code/Main.java"
    with open(name_file, mode="w", encoding="utf-8") as file_for_save:
        file_for_save.write(content)
    return name_file


def compile_code(path_to_java_file: str):
    try:
        res = subprocess.run(['javac', path_to_java_file], capture_output=True).stderr.decode()
        # print("res =\n", len(text))
        if len(res) == 0:
            res = "Поздравляем!\nКомпиляция прошла успешна!"
        else:
            res = f"Упс! возникли следующие ошибки:\n{res}"
        return res
    except Exception as ex:
        print("[ERROR] compile_code\n", ex)


def get_html_result_compiling(user_code: str):
    return compile_code(build_code_from_template(user_code))


if __name__ == '__main__':
    data = """System.out.println("Hello, world!")"""
    # name_file = "java_code/final_code/Main.java"
    # build_code_from_template(stroka)
    # print(compile_code(name_file))
    print(get_html_result_compiling(data))
