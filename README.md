# lms for learning to program

## Инструкция по запуску проекта

1. Создать папку для проекта

```
    mkdir lms_project
```

2. Создать в папке lms_program виртуальное окружение python через терминал
   командой:

```
    cd lms_project
    python -m venv venvLms
```

3. Клонировать в папку lms_program репозиторий с гитхаба:

```
   git clone https://github.com/Progger715/Platform-for-learning-to-program-.git
```

4. В проекте содержится файл req.txt все необходимы зависимости. Необходимо установить в виртуальное окружение
   все эти зависимости:

```
   cd venv_lms/bin
   cource activate
   which pip  // убедиться, что используется pip именно виртуального окружения 
   pip install -r [путь до файла req.txt, содержащегося в клонированном проекте]
```

5. /Platform-for-learning-to-program-/lms_programming/config создать файл с именем '.env' (без кавычек) и поместить в 
   файл следующую строку, **обязательно** добавив пустую строчку в конце):

```
SECRET_KEY=[ваш секретный ключ django без пробелов]

```

6. Для запуска проекта перейти в каталог lms_project и из виртуального активированного окржуения
   выполнить команду:

```
   python manage.py runserver 8000
```