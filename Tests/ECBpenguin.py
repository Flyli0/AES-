from AES.AESencoding import cipher
from AES.constants import block_size
#famous test for ecb insecurity

def ecb_encrypt(key, plaintext):#here i just done ecb without padding not to break image
    ciphertext = b""
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        ciphertext += cipher(key, block)
    return ciphertext


with open("peng.bmp", "rb") as f:#python image file handling
    data = f.read()

pixel_offset = int.from_bytes(data[10:14], "little")#bmp is very conveniently separates picture to head and body

header = data[:pixel_offset]
body = data[pixel_offset:]

key = bytes.fromhex(input("Insert hex key:\n"))

cut_len = len(body) - (len(body) % 16)

body_main = body[:cut_len]
body_tail = body[cut_len:]

encrypted_body = ecb_encrypt(key, body_main)

with open("penguin_ecb.bmp", "wb") as f:
    f.write(header + encrypted_body + body_tail)

print("Done! Saved as penguin_ecb.bmp")
#result into penguin_ecb.bmp and that was sooooooooooooooooooo long in time that i several times thought that programm isn't working