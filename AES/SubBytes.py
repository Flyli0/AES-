from AES.constants import Sbox
from AES.constants import InvSbox
def subBytes(state):
    for i in range(16):
        state[i] = Sbox[state[i]]

def inv_sub_bytes(state):
    for i in range(16):
        state[i] = InvSbox[state[i]]