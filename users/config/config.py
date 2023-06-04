import os
from pathlib import Path


def load_dotenv():
    path = Path(Path.cwd(), "users", "config", ".env")
    # path = Path("config", ".env")
    # path = Path(Path.cwd(), ".env")
    print(path)
    with open(path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        os.environ[line[:line.find('=')]] = line[line.find('=') + 1: line.find('\\')]


load_dotenv()

KEY_ENCRYPTION = os.environ['KEY_ENCRYPTION'].encode()
HASH_FUNCTION = os.environ['HASH_FUNCTION']
if __name__ == '__main__':
    print(type(KEY_ENCRYPTION))
    print(type(KEY_ENCRYPTION.encode()))
    print(KEY_ENCRYPTION.encode())
