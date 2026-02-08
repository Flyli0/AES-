def xor(block_1, block_2):
    return bytes(byte_1 ^ byte_2 for byte_1, byte_2 in zip(block_1, block_2))