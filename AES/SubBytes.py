from AES.constants import Sbox
from AES.constants import InvSbox
def subBytes(state):#using of an s-box to add nonlinearity into our cipher
    for i in range(16):
        state[i] = Sbox[state[i]]

def inv_sub_bytes(state):#inverse
    for i in range(16):
        state[i] = InvSbox[state[i]]