# import libraries
from pwn import *
from ast import literal_eval
import sys

# set recursion limit
sys.setrecursionlimit(10000)

# set some constants
TCP_IP = 'misc.chal.csaw.io'
TCP_PORT = 9000
MATRIX_POW = 6

# draw a s x s checkerboard
def drawBoard(s, dct=dict()):
    import sys
    if len(dct) == 0:
        for i in range(s):
            for j in range(s):
                dct[i, j] = [0, False]
    for i in range(s):
        sys.stdout.write(" _")
    sys.stdout.write("\n")
    for i in range(s):
        for j in range(s):
            if dct[i, j][0] == 0 or dct[i, j][0] == 201 \
               or dct[i, j][0] == 211 or dct[i, j][0] == 220 \
               or dct[i, j][0] == 222 or dct[i, j][0] == 232:
                sys.stdout.write("|_")
            elif dct[i, j][0] == 200 or dct[i, j][0] == 210 \
                 or dct[i, j][0] == 230:
                sys.stdout.write("| ")
            elif dct[i, j][0] == 202 or dct[i, j][0] == 212 \
                 or dct[i, j][0] == 231:
                sys.stdout.write(" _")
            elif dct[i, j][0] == 221:
                sys.stdout.write("  ")
            elif dct[i, j][0] == 1:
                sys.stdout.write("|" + "X")
        sys.stdout.write("|\n")
    print("")

# solve a triomono problem
def solve(n, start_x, start_y):
    import random
    side = 2**n
    d = dict()
    for i in range(side):
        for j in range(side):
            d[i, j] = [0, False]
    d[start_x, start_y] = [1, True]
    recurSolve([0, side-1], [0, side-1], side, d)
    print "[?] Final matrix is: "
    drawBoard(side, d) 

# helper function for solve()
def recurSolve(r, c, s, d):

    global count

    # if the board is 2x2, identify the 'marked' square and fill in the remaining three squares
    if r[1] - r[0] == 1:
        if d[r[0], c[0]][1]:
            count = count + 3
            send_point(r[0], c[1], r[1], c[0], r[1], c[1])
            d[r[0], c[1]][0] = 200
            d[r[1], c[0]][0] = 201
            d[r[1], c[1]][0] = 202
        elif d[r[0], c[1]][1]:
            count = count + 3
            send_point(r[0], c[0], r[1], c[0], r[1], c[1])
            d[r[0], c[0]][0] = 210
            d[r[1], c[0]][0] = 211
            d[r[1], c[1]][0] = 212
        elif d[r[1], c[0]][1]:
            count = count + 3
            send_point(r[0], c[0], r[0], c[1], r[1], c[1])
            d[r[0], c[0]][0] = 220
            d[r[0], c[1]][0] = 221
            d[r[1], c[1]][0] = 222
        elif d[r[1], c[1]][1]:
            count = count + 3
            send_point(r[0], c[0], r[0], c[1], r[1], c[0])
            d[r[0], c[0]][0] = 230
            d[r[0], c[1]][0] = 231
            d[r[1], c[0]][0] = 232
        return

    # the board is NOT 2x2, in which case we divide into four equally sized boards
    maxR = r[1]
    minR = r[0]
    maxC = c[1]
    minC = c[0]
    subMaxR = minR + (maxR - minR) // 2
    subMinR = subMaxR + 1
    subMaxC = minC + (maxC - minC) // 2
    subMinC = subMaxC + 1
    f1 = False
    f2 = False
    f3 = False
    f4 = False
    for r in range(minR, maxR+1):
        for c in range(minC, maxC+1):
            if r <= subMaxR and c <= subMaxC:
                if d[r, c][1]:
                    f1 = True
            elif r <= subMaxR and c > subMaxC:
                if d[r, c][1]:
                    f2 = True
            elif r > subMaxR and c <= subMaxC:
                if d[r, c][1]:
                    f3 = True
            elif r > subMaxR and c > subMaxC:
                if d[r, c][1]:
                    f4 = True
    if f1:
        count = count + 3
        send_point(subMaxR, subMinC, subMinR, subMaxC, subMinR, subMinC)
        d[subMaxR, subMinC] = [200, True]
        d[subMinR, subMaxC] = [201, True]
        d[subMinR, subMinC] = [202, True]
    elif f2:
        count = count + 3
        send_point(subMaxR, subMaxC, subMinR, subMaxC, subMinR, subMinC) 
        d[subMaxR, subMaxC] = [210, True]
        d[subMinR, subMaxC] = [211, True]
        d[subMinR, subMinC] = [212, True]
    elif f3:
        count = count + 3
        send_point(subMaxR, subMaxC, subMaxR, subMinC, subMinR, subMinC) 
        d[subMaxR, subMaxC] = [220, True]
        d[subMaxR, subMinC] = [221, True]
        d[subMinR, subMinC] = [222, True]
    elif f4:
        count = count + 3
        send_point(subMaxR, subMaxC, subMaxR, subMinC, subMinR, subMaxC) 
        d[subMaxR, subMaxC] = [230, True]
        d[subMaxR, subMinC] = [231, True]
        d[subMinR, subMaxC] = [232, True]
    recurSolve([minR, subMaxR], [minC, subMaxC], s, d)
    recurSolve([minR, subMaxR], [subMinC, maxC], s, d)
    recurSolve([subMinR, maxR], [minC, subMaxC], s, d)
    recurSolve([subMinR, maxR], [subMinC, maxC], s, d)

# get initial point
def get_point():

    # get lines
    r.recvuntil('marked block: ', drop=True)
    data = r.recvuntil('\n', drop=True)
    return data

# send a point to server
def send_point(x1, y1, x2, y2, x3, y3):

    global message
    message = message + "(" + str(x1) + "," + str(y1) + "),(" + str(x2) + "," + str(y2) +  "),(" + str(x3) + "," + str(y3) + ")\n"

# connect to server
r = remote(TCP_IP, TCP_PORT)
marked = literal_eval(get_point())
print "[?] Marked point is: " + str(marked)

# points init
points = []
points.append(marked)

# solve
count = 0
message = ""
solve(MATRIX_POW, marked[0], marked[1])
print "[+] Points added: " + str(count)
r.send(message)
flag = r.recvuntil('\n', drop=True)
print "[+] Your flag is: " + flag