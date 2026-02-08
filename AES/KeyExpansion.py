from AES.constants import Sbox
from AES.constants import Rcon

# 11223344556677889900aabbccddeeff

def rotWord(word):#rotates word by 1 to the left
    rot_word = word[1:] + word[:1]
    return rot_word


def subWord(word):#nonlinearity added by subsitution
    subword = [Sbox[b] for b in word]
    return subword


def rconXOR(word, roundnum):#to complecate keys even  moooore
    return [b ^ r for b, r in zip(word, Rcon[roundnum])]


def g(word, roundnum): #func for certain conditions to expand key
    rw = rotWord(word)
    sw = subWord(rw)
    sw = rconXOR(sw, roundnum)
    return bytes(sw)


def xor_words(a, b):#just xor
    return bytes(x ^ y for x, y in zip(a, b))

def Expand(secret):#main expanding func
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
    words = [secret[i:i + 4] for i in range(0, len(secret), 4)] #dividing our main key on several words

    for i in range(Nk, Nkeys):#filling needed number of words with empty 4-bytes sets to change them in future
        words.append(bytes(4))

    for i in range(Nk, Nkeys): #Expansion cycle
        temp = words[i - 1] #temporary variable to store last word
        if i % Nk == 0: #expansion conditions from FIPS-197
            temp = g(temp, i // Nk)
        elif Nk == 8 and i % Nk == 4:
            temp = bytes(subWord(temp))
        words[i] = xor_words(words[i - Nk], temp)#mandatory for all cases

    for i in range(0, len(words), 4):#adding completed keys to array of roundkeys
        roundkeys.append(b''.join(words[i:i + 4]))

    return roundkeys
