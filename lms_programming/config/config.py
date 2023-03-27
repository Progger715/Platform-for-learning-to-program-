import os
from pathlib import Path


def load_dotenv():
    path = Path(Path.cwd(), "lms_programming", "config", ".env")
    # print(path)
    with open(path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        os.environ[line[:line.find('=')]] = line[line.find('=') + 1: line.find('\\')]


load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
