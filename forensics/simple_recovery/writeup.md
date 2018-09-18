# CSAW CTF 2018: simple_recovery
![date](https://img.shields.io/badge/date-16.09.2018-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![forensics category](https://img.shields.io/badge/category-forensics-lightgrey.svg)
![score](https://img.shields.io/badge/score-150-blue.svg)
![solves](https://img.shields.io/badge/solves-306-brightgreen.svg)

## Description
Simple Recovery. Try to recover the data from these RAID 5 images!

## Attached files
- [disk.img1.7z](/disk.img1.7z)
- [disk.img2.7z](/disk.img2.7z)

## Summary
`strings` and `grep` under the recovered RAID 5 disk

## Flag
```
flag{dis_week_evry_week_dnt_be_securty_weak}
```

## Detailed solution
We use a *C* program from *Github*, called *[xor-files.c](https://github.com/scangeo/xor-files/blob/master/source/xor-files.c)*, to XOR the given disks.  
With a *Python* script, used in *deadnas* challenge [write-up](https://codisec.com/tw-mma-2-2016-deadnas/) from *Tokyo Westerns MMA CTF 2nd 2016*, considering the parity byes, we get a new recovered disk. Using `strings` over that, in combination with `grep “flag”`, we get the flag in plaintext.