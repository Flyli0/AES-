from AESencoding import cipher
from AESdecoding import decryption

block_hex = input("Insert 16 bytes \n")
block = bytes.fromhex(block_hex)


print("Plaintext:", block.hex())

state = cipher(block)
print("Ciphertext:", state.hex())


plain = decryption(state)
print("Decrypted:", plain.hex())
