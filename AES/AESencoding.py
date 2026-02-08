from AES.KeyExpansion import Expand
from AES.constants import roundnum
from AES.SubBytes import subBytes
from AES.ShiftRow import shiftRows
from AES.MixColumn import mixColumns


def cipher(key,block): #AES encoding
    #block = block.encode("utf-8")
    secret = key
    Nr = roundnum(secret)
    roundkeys = Expand(secret)
    state = bytearray(p ^ k for p, k in zip(block, roundkeys[0])) #state is created as pairing of bytes of plaintext and roundkey 0
    for i in range(1, Nr):#main cycle Nr = rounds
        subBytes(state)
        shiftRows(state)
        mixColumns(state)
        state = bytearray(p ^ k for p, k in zip(state, roundkeys[i]))

    subBytes(state)
    shiftRows(state)
    state = bytearray(p ^ k for p, k in zip(state, roundkeys[Nr]))
    return state







