<p align="center"><img src="https://user-images.githubusercontent.com/95581741/210697635-658e8729-2983-4d53-8c3c-97044b500cd9.jpg" width="570" alt="Hedgehog"></p>

<div align="center" style="margin-top: 0;">
   <h1>🦔 Hedgehog Encoder 🔒</h1>
</div>

This repository contains a simple encryption tool called HedgehogEncoder. It uses the AES algorithm in CTR mode with a randomly generated IV to encrypt and decrypt data. The tool takes in a password and uses it to generate a key for the encryption. The data is then encoded as a base64 string and random characters are inserted every 4 characters to make it harder to identify the encoding.

The HedgehogEncoder class has two methods: encode and decode. The encode method can be used to encrypt data and the decode method can be used to decrypt it.

This tool is useful for anyone who needs to encrypt and decrypt data in a simple and secure manner. It is written in Python and has no external dependencies.

# Usage
To use this encoder, you need to create an instance of the HedgehogEncoder class by providing it with a password and an initialization vector (IV). The IV can be randomly generated or can be obtained from another source.
```py
encoder = HedgehogEncoder(password, iv)
```
---
The encode method can be used to encrypt data and the decode method can be used to decrypt it.
```py
encrypted_data = encoder.encode(data)
decrypted_data = encoder.decode(encrypted_data)
```
---
# Example
```py
from HedgehogEncoder import HedgehogEncoder
import base64
import hashlib
import random
import string

# Initialize the encoder with a password and IV
password = "mypassword"
iv = "randomiv123456"
encoder = HedgehogEncoder(password, iv)

# Encrypt the data
data = "This is my secret message."
encrypted_data = encoder.encode(data)
print(encrypted_data)  # Output: "QkdKfjds1bsdjf9sdjf"

# Decrypt the data
decrypted_data = encoder.decode(encrypted_data)
print(decrypted_data)  # Output: "This is my secret message."
```

###### Hedgehogs have a unique type of skin that is covered in spines or quills. These spines are actually modified hairs that are stiff and sharp, and they serve as a defense mechanism against predators. The spines are usually brown or black in color and are found all over the hedgehog's body, except for its face, ears, and underbelly. When threatened, a hedgehog will roll into a tight ball, presenting its spines as a barrier to protect itself. While the spines may look intimidating, they are actually relatively soft to the touch and do not cause any harm when handled carefully.
