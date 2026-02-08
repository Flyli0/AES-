from time import time_ns
from os import getpid
from AES.constants import m
from AES.constants import a
from AES.constants import c

# Function that takes byte count to generate and returns pseudo-randomly generated 
# sequence in bytes type
def random_bytes(byte_count):
    # time in nanoseconds since the epoch and process ID are XORed
    pseudo_random_value = time_ns() ^ getpid()
    result = b""
    while len(result) < byte_count:
        pseudo_random_value = (a * pseudo_random_value + c) % m
        result += pseudo_random_value.to_bytes(8, "big")
    return result[:byte_count]

