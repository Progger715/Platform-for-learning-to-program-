from cryptography.fernet import Fernet
from users.config import config
import os
import hashlib


def encrypt_data(data: str):
    cipher_suite = Fernet(config.KEY_ENCRYPTION)  # Создание объекта для шифрования с использованием ключа
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text


def decrypt_data(data: str):
    cipher_suite = Fernet(config.KEY_ENCRYPTION)  # Создание объекта для дешифрования с использованием ключа
    cipher_text = cipher_suite.decrypt(data)
    return cipher_text


def hash_data(data: str, salt: bytes):
    hashed_data = hashlib.pbkdf2_hmac(
        config.HASH_FUNCTION,
        data.encode('utf-8'),
        salt,
        200000,
        dklen=64
    )
    return hashed_data


# print(f"default = {encrypt_data('null')}")
