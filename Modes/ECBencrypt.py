from AES.AESencoding import cipher
from Padding.Padding import padding_func
from AES.constants import block_size

# Function for ECB encryption, takes key and plaintext of bytes type, returns 
# ciphertext of bytes type
def ecb_encrypt(key,plaintext):
    plaintext = padding_func(plaintext, block_size)
    ciphertext = b""
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        ciphertext += cipher(key, block)
    return ciphertext




