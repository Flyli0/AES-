from KeyExpansion import roundkeys
from KeyExpansion import Nr
from SubBytes import subBytes
block_hex = input("Insert 16 bytes \n")
block = bytes.fromhex(block_hex)
print(block)
print('Success')

state = bytearray(p^k for p,k in zip(block,roundkeys[0])) #Тут создаю массив стейт который хорит сразу инишл ки и наш блок 128бит

for i in range(Nr):
    state = subBytes(state)





