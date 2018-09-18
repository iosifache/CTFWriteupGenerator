# CSAW CTF 2018: Algebra
![date](https://img.shields.io/badge/date-16.09.2018-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-100-blue.svg)
![solves](https://img.shields.io/badge/solves-410-brightgreen.svg)

## Description
Are you a real math wiz?  
```nc misc.chal.csaw.io 9002```

## Summary
Using **sympy** library in *Python*, solve the equations given by server

## Flag
```
flag{y0u_s0_60od_aT_tH3_qU1cK_M4tH5}
```

## Detailed solution
We need to create a *Python* script that takes over the equations given by server and solves it.  
For scrapping the server response, we use **pwntools** modules with its function `recvutil()`. For solving equation(that must be equal to 0), we use **sympy** module after a little processing of string equation(replace equal to minus).  
After repeated results sended to server, we receive the flag.