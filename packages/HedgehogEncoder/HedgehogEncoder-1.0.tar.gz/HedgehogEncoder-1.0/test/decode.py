import base64
import binascii

import HedgehogEncoder

if __name__ == '__main__':
    iv = input("Enter the IV: ")
    try:
        iv = base64.b64decode(iv)
    except binascii.Error:
        print("Invalid IV")
        exit()
    passowrd = input("Enter the password: ")
    while True:
        Hedge = HedgehogEncoder.HedgehogEncoder(passowrd, iv)
        encoded = Hedge.decode(input("Enter a message to Decode: "))
        print(f"Decoded: {encoded}")
