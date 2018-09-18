# CSAW CTF 2018: Take an L
![date](https://img.shields.io/badge/date-16.09.2018-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-200-blue.svg)
![solves](https://img.shields.io/badge/solves-192-brightgreen.svg)

## Description
Fill the grid with L's but avoid the marked spot for the W. The origin is at (0,0) on the top left.
`nc misc.chal.csaw.io 9000`    

## Attached files
- [description.pdf](/description.pdf)

## Summary
Solve a given **triominos problem**

## Flag
```
flag{m@n_that_was_sup3r_hard_i_sh0uld_have_just_taken_the_L}
```

## Detailed solution
After making a little research, we find out that this is a *Divide et Impera algorithm*, more specific a *triominos problem*.   
We find a Python [script](https://github.com/huckCussler/triomino_solver/blob/master/tri.py) on *Github* that solve this for a random point on the board. We modify it to accept the point that is given by the server and to return the *triominos* checked points. After solving it and construct the solution, we send it to server using **pwntools** and we receive the flag.