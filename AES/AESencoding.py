from AES.KeyExpansion import Expand
from AES.constants import roundnum
from AES.SubBytes import subBytes
from AES.ShiftRow import shiftRows
from AES.MixColumn import mixColumns


def cipher(key,block):
    #block = block.encode("utf-8")
    secret = key
    Nr = roundnum(secret)
    roundkeys = Expand(secret)
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







