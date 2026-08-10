from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


salt = b'\xbb\xa1:\x89\xc8\xcdKL\xdc\x7f^\xc5\xce)\x16"\xbd\xf6\xfaL\x05\x8e.I\xba\\q\xef\xbbb\x8f\xfb'

def encryption_key_gen(password):
    key = PBKDF2(password,salt, dkLen=32)
    return key
