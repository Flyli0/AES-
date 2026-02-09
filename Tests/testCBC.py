from Modes.CBCencrypt import cbc_encrypt
from Modes.CBCdecrypt import cbc_decrypt

key = bytes.fromhex(input("insert key"))
plaintext = input("insert plaintext")
plain = plaintext.encode("utf-8")

enc = cbc_encrypt(key, plain)
print(enc.hex())
print(str(cbc_decrypt(key, enc)))
 #