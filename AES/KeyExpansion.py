from AES import secret
from constants import Sbox
from constants import Rcon
#from AES import roundnum 11223344556677889900aabbccddeeff

def rotWord(word):
    rot_word = word[1:] + word[:1]
    return rot_word


def subWord(word):
    subword = [Sbox[b] for b in word]
    return subword


def rconXOR(word, roundnum):
    word[0] = Rcon[roundnum][0]
    word[1] = Rcon[roundnum][1]
    word[2] = Rcon[roundnum][2]
    word[3] = Rcon[roundnum][3]

def g(word,roundnum):
    rw = rotWord(word)
    sw = subWord(rw)
    rconXOR(sw,roundnum)
    return bytes(sw)

def xor_words(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

length = "128bit"
Nb = 4  # const
Nr = 10
Nk = 4  # because 128 bit = 16 bytes = 4 words
Nkeys = Nb * (Nr + 1)
keys = []
words = [secret[i:i + 4] for i in range(0, len(secret), 4)]
for i in range(4, Nkeys):
    words.append(bytes(4))
print(words)
for i in range(4, Nkeys):
    if i % Nk != 0:
        words[i] = xor_words(words[i-Nk],words[i-1])
        print(0)
    else:
        words[i] = xor_words(words[i-Nk],g(words[i-1],1))

print(words)