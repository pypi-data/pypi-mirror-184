import base64
import hashlib
import random
import string

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class HedgehogEncoder:
    def __init__(self, password, iv):
        self.backend = default_backend()
        # Hash the password to ensure it has sufficient entropy
        self.password = hashlib.sha256(password.encode()).digest()
        # Generate a key and initialization vector using the password
        self.key = hashlib.sha256(self.password).digest()
        self.iv = iv

    def encode(self, data):
        # Create a cipher using the key and IV
        cipher = Cipher(algorithms.AES(self.key), modes.CTR(self.iv), backend=self.backend)
        encryptor = cipher.encryptor()

        # Encrypt the data and encode it as a base64 string
        encrypted = encryptor.update(data.encode()) + encryptor.finalize()
        encoded = base64.b64encode(encrypted)

        # Insert a random character every 4 characters
        result = ""
        count = 0
        for c in encoded.decode():
            result += c
            count += 1
            if count % 4 == 0:
                result += random.choice(string.ascii_letters)
        return result

    def decode(self, encoded):
        # Remove the random characters inserted every 4 characters
        decoded = ""
        count = 0
        for c in encoded:
            if count % 5 == 4:
                count += 1
                continue
            decoded += c
            count += 1

        # Decode the modified base64 string and extract the encrypted data
        decoded = base64.b64decode(decoded)

        # Create a cipher using the key and IV
        cipher = Cipher(algorithms.AES(self.key), modes.CTR(self.iv), backend=self.backend)
        decryptor = cipher.decryptor()

        # Decrypt the data
        data = decryptor.update(decoded) + decryptor.finalize()
        return data.decode()
