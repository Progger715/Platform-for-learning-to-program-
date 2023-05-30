from cryptography.fernet import Fernet
from handler_code.config import config


def encrypt_data(data: str):
    cipher_suite = Fernet(config.KEY_ENCRYPTION)  # Создание объекта для шифрования с использованием ключа
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text


def decrypt_data(data: str):
    cipher_suite = Fernet(config.KEY_ENCRYPTION)  # Создание объекта для дешифрования с использованием ключа
    cipher_text = cipher_suite.decrypt(data.encode())
    return cipher_text
