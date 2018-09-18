# CSAW CTF 2018: flatcrypt
![date](https://img.shields.io/badge/date-16.09.2018-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![crypto category](https://img.shields.io/badge/category-crypto-lightgrey.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)
![solves](https://img.shields.io/badge/solves-184-brightgreen.svg)

## Description
No logos or branding for this bug. Take your pick:
```
nc crypto.chal.csaw.io 8040 
nc crypto.chal.csaw.io 8041 
nc crypto.chal.csaw.io 8042 
nc crypto.chal.csaw.io 8043
```  
Flag is not in flag format. Flag is PROBLEM_KEY.

## Attached files
- [serv-distribute.py](/serv-distribute.py)

## Summary
Compression attack over partially-controlled plaintext 

## Flag
```
crime_doesnt_have_a_logo
```

## Detailed solution
After analyzing the source code of the server, we learn that it is an **AES-CTR encryption**, combined with a **zlib compression**. The encrypted text is `PROBLEM_KEY`, concatenated with our text. The *counter* is initially random and increases over encrypting blocks.  
We use the compression method to steply guess the `PROBLEM_KEY`. For example, for the last letter(first guessed), we try all possible characters(`string.ascii_lowercase + "_"`, as they said in [serv-distribute.py](/serv-distribute.py)) and view what length is smaller than all others.  
To simplify our job, we create a *Python* script that tests all the possible combinations and prints the length of encrypted text(last byte of the response of server, `chr(len(enc))`).