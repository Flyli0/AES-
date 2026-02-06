from KeyExpansion import Expand
from constants import roundnum
from SubBytes import subBytes
from ShiftRow import shiftRows
from MixColumn import mixColumns




def cipher(block):
    key = input("Insert hex key\n")
    secret = bytes.fromhex(key)
    Nr = roundnum(secret)
    roundkeys = Expand(secret)
    print(roundkeys)
    state = bytearray(p ^ k for p, k in zip(block, roundkeys[0]))
    for i in range(1, Nr):
        subBytes(state)
        shiftRows(state)
        mixColumns(state)
        state = bytearray(p ^ k for p, k in zip(state, roundkeys[i]))

    subBytes(state)
    shiftRows(state)
    state = bytearray(p ^ k for p, k in zip(state, roundkeys[Nr]))
    return state







