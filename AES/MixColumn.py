def xtime(a): #GF offset rule
    if a & 0x80:
        return ((a << 1) ^ 0x1B) & 0xFF
    else:
        return (a << 1) & 0xFF


def mixColumns(state): #multiplying by polinomial hardcoded
    for c in range(4):
        i = c * 4 #because state is 1d array we mult i by 4 to access columns(state is filled by columns)
        s0 = state[i]
        s1 = state[i + 1]
        s2 = state[i + 2]
        s3 = state[i + 3]
        state[i] = xtime(s0) ^ (xtime(s1) ^ s1) ^ s2 ^ s3
        state[i + 1] = s0 ^ xtime(s1) ^ (xtime(s2) ^ s2) ^ s3
        state[i + 2] = s0 ^ s1 ^ xtime(s2) ^ (xtime(s3) ^ s3)
        state[i + 3] = (xtime(s0) ^ s0) ^ s1 ^ s2 ^ xtime(s3)


def inv_mix_column(state):
    def xtime(a):
        return ((a << 1) ^ 0x1B) & 0xFF if (a & 0x80) else (a << 1) & 0xFF

    def mul2(a):#multiplying different powers of 2
        return xtime(a)

    def mul3(a):
        return xtime(a) ^ a

    def mul9(a):
        return xtime(xtime(xtime(a))) ^ a

    def mul11(a):
        return xtime(xtime(xtime(a)) ^ a) ^ a

    def mul13(a):
        return xtime(xtime(xtime(a) ^ a)) ^ a

    def mul14(a):
        return xtime(xtime(xtime(a) ^ a) ^ a)

    for c in range(4):#inverse of previous process
        i = c * 4
        s0 = state[i]
        s1 = state[i + 1]
        s2 = state[i + 2]
        s3 = state[i + 3]
        state[i] = mul14(s0) ^ mul11(s1) ^ mul13(s2) ^ mul9(s3)
        state[i + 1] = mul9(s0) ^ mul14(s1) ^ mul11(s2) ^ mul13(s3)
        state[i + 2] = mul13(s0) ^ mul9(s1) ^ mul14(s2) ^ mul11(s3)
        state[i + 3] = mul11(s0) ^ mul13(s1) ^ mul9(s2) ^ mul14(s3)
