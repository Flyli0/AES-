from AESencoding import cipher
from AESdecoding import decryption

block_hex = input("Insert 16 bytes \n")
block = block_hex.encode("utf-8")


print("Plaintext:", block.hex())

state = cipher(block)
print("Ciphertext:", state.hex())


plain = decryption(state)
plain = plain.decode("utf-8")
print("Decrypted:", plain)
