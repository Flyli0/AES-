from ShiftRow import inv_shift_rows
from SubBytes import inv_sub_bytes
from MixColumn import inv_mix_column
from KeyExpansion import Nr
from KeyExpansion import roundkeys


def decryption(state):
    state = bytearray(p ^ k for p, k in zip(state, roundkeys[Nr]))

    for i in range(Nr-1, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        state = bytearray(p ^ k for p, k in zip(state, roundkeys[i]))
        inv_mix_column(state)

    inv_shift_rows(state)
    inv_sub_bytes(state)
    state = bytearray(p ^ k for p, k in zip(state, roundkeys[0]))
    return state
