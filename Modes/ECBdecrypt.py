from AES.AESdecoding import decryption
from Padding.Unpadding import unpadding_func
from AES.constants import block_size

def ecb_decrypt(key,ciphertext):
    plaintext = b""
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        plaintext += decryption(key,block)
    plaintext = unpadding_func(plaintext, block_size)
    return plaintext
