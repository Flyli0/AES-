from AES.AESencoding import cipher
from AES.constants import block_size
from Xor import xor

def ctr_decrypt(ciphertext):
    nonce = ciphertext[:12]
    plaintext = b""
    counter = 0

    for i in range(12, len(ciphertext), block_size):
        ciphertext_block = ciphertext[i:i + block_size]
        counter_block = nonce + counter.to_bytes(4, byteorder="big")
        keystream_block = cipher(counter_block)
        plaintext_block = xor(ciphertext_block, keystream_block[:len(ciphertext_block)])
        plaintext += plaintext_block
        counter += 1

    return plaintext
