from AES.AESdecoding import decryption
from Padding.Padding import unpadding_func
from AES.constants import block_size
from Rand.RandomBytes import random_bytes
from Xor import xor

def cbc_decrypt(ciphertext):
    iv = ciphertext[:block_size]
    plaintext = b""
    previous_ciphertext_block = iv

    for i in range(block_size, len(ciphertext), block_size):
        ciphertext_block = ciphertext[i:i+block_size]
        decrypted_block = decryption(ciphertext_block)  
        plaintext_block = xor(decrypted_block, previous_ciphertext_block)
        plaintext += plaintext_block
        previous_ciphertext_block = ciphertext_block

    plaintext = unpadding_func(plaintext, block_size)
    return plaintext
