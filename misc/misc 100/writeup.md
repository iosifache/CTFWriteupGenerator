# Tren Micro CTF 2018 Quals: Misc 100

![date](https://img.shields.io/badge/date-15.09.2018-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)

## Description
Recover the flag from a PDF file  

## Attached files
- [EATME.pdf](/EATME.pdf)

## Summary
Search in **hex data** of *EATME.pdf* and find an archive that contain the flag(inside a file named *flag.txt*)

## Flag
```
TMCTF{QWxpY2UgaW4gV29uZGVybGFuZA==}
```

## Detailed solution
We open *EATME.pdf* with **HxD** on *Windows* and search for string *flag*. We find on index *000B6DD0-08* **magic bytes PK**, corresponding to another archive. 
Copy the data inside a *.zip* file and extract it. In file *flag.txt*, we find the plaintext flag.