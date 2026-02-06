from AES.AESencoding import cipher
from Padding.Padding import padding_func
from AES.constants import block_size
from Rand.RandomBytes import random_bytes

def xor(block_1, block_2):
    return bytes(byte_1 ^ byte_2 for byte_1, byte_2 in zip(block_1, block_2))

def cbc_encrypt(plaintext):
    plaintext = padding_func(plaintext, block_size)
    iv = random_bytes(block_size)
    ciphertext = iv  
    previous_ciphertext_block = iv

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        xored_block = xor(block, previous_ciphertext_block)
        ciphertext_block = cipher(xored_block)
        ciphertext += ciphertext_block
        previous_ciphertext_block = ciphertext_block

    return ciphertext
