# CSAW CTF 2018: bin_t

![date](https://img.shields.io/badge/date-16.09.2018-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)  
![misc category](https://img.shields.io/badge/category-misc-lightgrey.svg)
![score](https://img.shields.io/badge/score-50-blue.svg)
![solves](https://img.shields.io/badge/solves-334-brightgreen.svg)

## Description
Binary trees let you do some interesting things. Can you balance a tree?  
```nc misc.chal.csaw.io 9001```  
Equal nodes should be inserted to the right of the parent node. You should balance the tree as you add nodes.

## Summary
Create a Python script that inserts all values given by server into an AVL tree and that traverse it in preorder

## Flag
```
flag{HOW_WAS_IT_NAVIGATING_THAT_FOREST?}
```

## Detailed solution
We find a [gist](https://gist.github.com/girish3/a8e3931154af4da89995) with an implementation of *AVL trees* in *Python*. Over this code, we construct  our preorder traverse function, `preorder_traverse()`.  
In the main script, we get the values(that must be entered in the tree) with **pwntools**. After that, these values are introduced into a new `AVLTree` object and we call `preorder_traverse()` function whose result is sent to the server. Then, we receive the flag.