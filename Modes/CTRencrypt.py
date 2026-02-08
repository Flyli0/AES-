from AES.AESencoding import cipher
from AES.constants import block_size
from Rand.RandomBytes import random_bytes
from Modes.Xor import xor

# Function for CTR encryption, takes key and plaintext of bytes type, returns 
# ciphertext of bytes type
def ctr_encrypt(key,plaintext):
    nonce = random_bytes(12)  
    ciphertext = nonce
    counter = 0

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        counter_block = nonce + counter.to_bytes(4, byteorder="big")
        keystream_block = cipher(key,counter_block)
        ciphertext_block = xor(block, keystream_block[:len(block)])
        ciphertext += ciphertext_block
        counter += 1

    return ciphertext
