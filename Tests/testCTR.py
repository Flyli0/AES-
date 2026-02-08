from Modes.CTRencrypt import ctr_encrypt
from Modes.CTRdecrypt import ctr_decrypt

key = bytes.fromhex(input("insert key"))
plaintext = input("insert plaintext")
plain = plaintext.encode("utf-8")

enc = ctr_encrypt(key, plain)
print(enc)
print(ctr_decrypt(key, enc))