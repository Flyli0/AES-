from AES.AESencoding import cipher
from Padding.Padding import padding_func
from AES.constants import block_size

def ecb_encrypt(key,plaintext):
    plaintext = padding_func(plaintext, block_size)
    ciphertext = b""
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        ciphertext += cipher(key, block)
    return ciphertext