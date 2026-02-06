from KeyExpansion import roundkeys
from KeyExpansion import Nr
from SubBytes import subBytes
from ShiftRow import shiftRows
from MixColumn import mixColumns
block_hex = input("Insert 16 bytes \n")
block = bytes.fromhex(block_hex)
print(block)
print('Success')

state = bytearray(p^k for p,k in zip(block,roundkeys[0]))

for i in range(1,Nr):
    subBytes(state)
    shiftRows(state)
    mixColumns(state)
    state = bytearray(p^k for p,k in zip(state,roundkeys[i]))

subBytes(state)
shiftRows(state)
state = bytearray(p^k for p,k in zip(state,roundkeys[Nr]))

print(state.hex())




