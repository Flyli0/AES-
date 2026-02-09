from AES.AESencoding import cipher
from Padding.Padding import padding_func
from AES.constants import block_size
from Rand.RandomBytes import random_bytes
from Modes.Xor import xor

# Function for CBC encryption, takes key and plaintext of bytes type, returns 
# ciphertext of bytes type
def cbc_encrypt(key,plaintext):
    plaintext = padding_func(plaintext, block_size)
    iv = random_bytes(block_size)
    ciphertext = iv  
    previous_ciphertext_block = iv

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        xored_block = xor(block, previous_ciphertext_block)
        ciphertext_block = cipher(key,xored_block)
        ciphertext += ciphertext_block
        previous_ciphertext_block = ciphertext_block

    return ciphertext
