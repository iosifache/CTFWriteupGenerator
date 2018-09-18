# import libraries
import string
from pwn import *

# define some constants
TCP_IP = "crypto.chal.csaw.io"
TCP_PORT = "8040"
ALREADY_GUESSED = "crime_doesnt_have_a_logo"
MIN_LENGHT = 32

# make connection
r = remote(TCP_IP, TCP_PORT)
data = r.recvuntil('\n', drop=True)
for i in (string.ascii_lowercase + "_"):
    if len(ALREADY_GUESSED) != 0:
        payload = (i + ALREADY_GUESSED) * (MIN_LENGHT/len(ALREADY_GUESSED) + 1)
    else:
        payload = i * MIN_LENGHT
    r.send(payload + "\n")
    data = r.recvuntil('Encrypting service', drop=True)
    print "[+] Send payload: " + payload + " with ciphertext lenght of " + str(ord(data[len(data) - 2]))