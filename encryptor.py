from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

class FileEncryptor:
    def __init__(self, encrypted_file_path, key_file_path, password=b'senha_segura'):
        self.encrypted_file_path = encrypted_file_path
        self.key_file_path = key_file_path
        self.password = password
    
    def _generate_key(self, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(self.password)

    def _encrypt_content(self, content: str):
        salt = os.urandom(16)
        key = self._generate_key(salt)
        iv = os.urandom(16)

        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(content.encode()) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        with open(self.encrypted_file_path, 'wb') as file:
            file.write(iv + encrypted_data)

        with open(self.key_file_path, 'wb') as file:
            file.write(salt)

    def _decrypt_content(self) -> str:
        try:
            with open(self.key_file_path, 'rb') as file:
                salt = file.read(16)
                if len(salt) != 16:
                    raise ValueError("Invalid or corrupt Salt.")
            key = self._generate_key(salt)

            with open(self.encrypted_file_path, 'rb') as file:
                iv = file.read(16)
                if len(iv) != 16:
                    raise ValueError("Invalid or corrupted IV.")
                encrypted_data = file.read()
                if len(encrypted_data) == 0:
                    raise ValueError("Missing or corrupt encrypted data.")

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

            unpadder = padding.PKCS7(128).unpadder()
            decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

            return decrypted_data.decode()

        except ValueError as e:
            print(f"Error during decryption: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def add_key_value_pair(self, key: str, value: str):
        if os.path.exists(self.encrypted_file_path):
            current_content = self._decrypt_content()
        else:
            current_content = ""
        
        updated_content = f"{current_content}\n{key}:{value}".strip()
        self._encrypt_content(updated_content)

    def get_all_pairs(self):
        if not os.path.exists(self.encrypted_file_path):
            return {}

        decrypted_content = self._decrypt_content()

        pairs = {}
        for line in decrypted_content.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                pairs[k] = v

        return pairs
