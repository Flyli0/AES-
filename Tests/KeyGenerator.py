from Rand.RandomBytes import random_bytes

def generate(size_bits):
    size_bytes = size_bits // 8
    key = random_bytes(size_bytes)
    return key.hex()
