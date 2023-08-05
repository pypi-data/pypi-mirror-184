import base64
import binascii
import os

import HedgehogEncoder

if __name__ == '__main__':
    iv = input("Enter the IV or Enter For Generate: ")
    if iv == "":
        iv = os.urandom(16)
    else:
        try:
            iv = base64.b64decode(iv)
        except binascii.Error:
            print("Invalid IV")
            exit()
    print("IV:", base64.b64encode(iv).decode("utf-8"))
    passowrd = input("Enter the password: ")
    while True:
        Hedge = HedgehogEncoder.HedgehogEncoder(passowrd, iv)
        encoded = Hedge.encode(input("Enter a message to encode: "))
        print(f"Encoded: {encoded}")