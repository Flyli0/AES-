from AES.AESdecoding import decryption
from Padding.Padding import unpadding_func
from AES.constants import block_size

def ecb_decrypt(ciphertext):
    plaintext = b""
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        plaintext += decryption(block)
    plaintext = unpadding_func(plaintext, block_size)
    return plaintext
