from Modes.ECBencrypt import ecb_encrypt
from Modes.ECBdecrypt import ecb_decrypt
#general tests for each type and AES itself
'''block = input("Insert 16 bytes \n")
#8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b


print("Plaintext:", block)

state = cipher(key, block)
print("Ciphertext:", state.hex())


plain = decryption(key, state)
plain = plain.decode("utf-8")
print("Decrypted:", plain)'''

key = bytes.fromhex(input("Insert hex key:\n"))
text = input()
print("plaintext: ", text)
text = text.encode("utf-8")
ciphertext = ecb_encrypt(key,text)
print("encrypted: ", ciphertext.hex())
plain = ecb_decrypt(key,ciphertext)
print("decrypted: ", plain)
