def padding_func(plaintext, block_size):
    padding_len = block_size - (len(plaintext) % block_size)
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding
