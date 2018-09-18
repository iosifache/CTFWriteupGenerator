# import libraries
from pwn import *

# import avl from 'https://gist.github.com/girish3/a8e3931154af4da89995'
import avl

# set some constants
TCP_IP = 'misc.chal.csaw.io'
TCP_PORT = 9001

# get encrypted flag
def get_nodes():

    # get lines
    r.recvuntil('\n', drop=True)
    data = r.recvuntil('\n', drop=True)
    r.recvuntil('\n', drop=True)

    # delete '/r' from end and convert to integer
    intermediar = list(data)[:-1]
    data = ''.join(intermediar)

    # return
    return data.split(",")

# make connection and take nodes
r = remote(TCP_IP, TCP_PORT)
nodes = get_nodes()
print "[+] Nodes are: "
new = [int(x) for x in nodes]

# avl init and insert
tree = AVLTree()
for n in new: 
    tree.insert(n)

# preorder traverse
preorder_list = tree.preorder_traverse()
preorder = ",".join(str(elem) for elem in preorder_list)
print "[+] Preorder traverse is: " + preorder

# send result and get flag
r.send(preorder + "\n")
flag = r.recvuntil('\n', drop=True)
print "[+] Flag is: " + flag