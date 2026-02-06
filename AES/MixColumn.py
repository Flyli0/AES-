def xtime(a): #Правило сдвига по GF
    if a & 0x80:
        return ((a << 1) ^ 0x1B) & 0xFF
    else:
        return (a << 1) & 0xFF


def mixColumns(state):
    for c in range(4):
        i = c * 4
        s0 = state[i]
        s1 = state[i + 1]
        s2 = state[i + 2]
        s3 = state[i + 3]
        state[i] = xtime(s0) ^ (xtime(s1) ^ s1) ^ s2 ^ s3
        state[i + 1] = s0 ^ xtime(s1) ^ (xtime(s2) ^ s2) ^ s3
        state[i + 2] = s0 ^ s1 ^ xtime(s2) ^ (xtime(s3) ^ s3)
        state[i + 3] = (xtime(s0) ^ s0) ^ s1 ^ s2 ^ xtime(s3)
