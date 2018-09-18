# import libraries
import zlib
import os
import string
from Crypto.Cipher import AES
from Crypto.Util import Counter

# determine PROBLEM_KEY(lowercase letters and underscore)
ENCRYPT_KEY = bytes(bytearray.fromhex('0000000000000000000000000000000000000000000000000000000000000000'))
PROBLEM_KEY = 'not_the_flag'
ALREADY_GUESSED = ""
MIN_LENGHT = 32

# encrypt function
def encrypt(data, ctr):
    return AES.new(ENCRYPT_KEY, AES.MODE_CTR, counter=ctr).encrypt(zlib.compress(data))

# encryption service
def service(): 
    while True:

        # read input
        f = raw_input("Encrypting service\n")
        if len(f) < 20:
            continue
        
        # encrypt (PROBLEM_KEY + input), encoded as UTF-8 with 64-bit counter, with 64-bit random prefix
        enc = encrypt(bytes((PROBLEM_KEY + f).encode('utf-8')), Counter.new(64, prefix=os.urandom(8)))
        print("%s%s" %(enc, chr(len(enc))))