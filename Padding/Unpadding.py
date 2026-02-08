# Function that takes padded plaintext in bytes type and block size in bytes and 
# returns unpadded plaintext
def unpadding_func(padded_plaintext, block_size):
    if len(padded_plaintext) == 0 or len(padded_plaintext) % block_size != 0:
        raise ValueError("Invalid padded plaintext length")

    padding_len = padded_plaintext[-1]

    if padding_len < 1 or padding_len > block_size:
        raise ValueError("Invalid padding length")

    if padded_plaintext[-padding_len:] != bytes([padding_len] * padding_len):
        raise ValueError("Invalid padding")

    return padded_plaintext[:-padding_len]
