from time import time_ns
from os import getpid
from AES.constants import m
from AES.constants import a
from AES.constants import c

def random_bytes(byte_count):
    pseudo_random_value = time_ns() ^ getpid()
    result = b""
    while len(result) < byte_count:
        pseudo_random_value = (a * pseudo_random_value + c) % m
        result += pseudo_random_value.to_bytes(8, "big")
    return result[:byte_count]

