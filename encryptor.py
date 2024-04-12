import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet



class Encryptor:
    def __init__(self, key):
        self.key = key
        self.cache = {}

    async def encrypt(self, text):
        if text in self.cache:
            return self.cache[text]

        salt = b'\x00' * 16  
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.key.encode()))
        cipher = Fernet(key)
        encrypted_text = cipher.encrypt(text.encode())
        self.cache[text] = encrypted_text
        return encrypted_text

    async def decrypt(self, encrypted_text):
        salt = b'\x00' * 16  
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.key.encode()))
        cipher = Fernet(key)
        decrypted_text = cipher.decrypt(encrypted_text).decode()
        return decrypted_text