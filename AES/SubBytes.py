from constants import Sbox
def subBytes(state):
    for i in range(16):
        state[i] = Sbox[state[i]]
    return state
