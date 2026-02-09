from AES.AESdecoding import decryption
from Padding.Unpadding import unpadding_func
from AES.constants import block_size
from Modes.Xor import xor

# Function for CBC decryption, takes key and ciphertext of bytes type, returns 
# plaintext of bytes type
def cbc_decrypt(key,ciphertext):
    iv = ciphertext[:block_size]
    plaintext = b""
    previous_ciphertext_block = iv

    for i in range(block_size, len(ciphertext), block_size):
        ciphertext_block = ciphertext[i:i+block_size]
        decrypted_block = decryption(key,ciphertext_block)
        plaintext_block = xor(decrypted_block, previous_ciphertext_block)
        plaintext += plaintext_block
        previous_ciphertext_block = ciphertext_block

    plaintext = unpadding_func(plaintext, block_size)
    return plaintext
