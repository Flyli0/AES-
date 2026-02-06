from constants import Sbox
from constants import Rcon

# 11223344556677889900aabbccddeeff

def rotWord(word):
    rot_word = word[1:] + word[:1]
    return rot_word


def subWord(word):
    subword = [Sbox[b] for b in word]
    return subword


def rconXOR(word, roundnum):
    return [b ^ r for b, r in zip(word, Rcon[roundnum])]


def g(word, roundnum):
    rw = rotWord(word)
    sw = subWord(rw)
    sw = rconXOR(sw, roundnum)
    return bytes(sw)


def xor_words(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def Expand(secret):
    if len(secret) == 16:
        Nk = 4
        Nr = 10
    elif len(secret) == 24:
        Nk = 6
        Nr = 12
    elif len(secret) == 32:
        Nk = 8
        Nr = 14
    else:
        raise ValueError("Key must be 16, 24, or 32 bytes")

    Nb = 4  # const
    Nkeys = Nb * (Nr + 1)
    roundkeys = []
    key = []
    count = 0
    words = [secret[i:i + 4] for i in range(0, len(secret), 4)]

    for i in range(Nk, Nkeys):
        words.append(bytes(4))

    for i in range(Nk, Nkeys):
        temp = words[i - 1]
        if i % Nk == 0:
            temp = g(temp, i // Nk)
        elif Nk == 8 and i % Nk == 4:
            temp = bytes(subWord(temp))
        words[i] = xor_words(words[i - Nk], temp)

    for i in range(0, len(words), 4):
        roundkeys.append(b''.join(words[i:i + 4]))

    return roundkeys
