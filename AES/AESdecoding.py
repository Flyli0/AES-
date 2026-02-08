from AES.ShiftRow import inv_shift_rows
from AES.SubBytes import inv_sub_bytes
from AES.MixColumn import inv_mix_column
from AES.constants import roundnum
from AES.KeyExpansion import Expand

def decryption(key,state): #Decryption function

    secret = key
    Nr = roundnum(secret)
    roundkeys = Expand(secret)
    state = bytearray(p ^ k for p, k in zip(state, roundkeys[Nr])) #state is created as pairing of corresponding bytes through zip func

    for i in range(Nr-1, 0, -1):
        inv_shift_rows(state)#inverse function of shift rows
        inv_sub_bytes(state)#inverse sub bytes
        state = bytearray(p ^ k for p, k in zip(state, roundkeys[i])) #adding roundkey by xoring it with text
        inv_mix_column(state)#mix column
    #last round without mix column reverse
    inv_shift_rows(state)
    inv_sub_bytes(state)
    state = bytearray(p ^ k for p, k in zip(state, roundkeys[0]))
    return state
