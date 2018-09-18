# import libraries
from pwn import *
from sympy.solvers import solve
from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr
from sympy import *

# set some constants
TCP_IP = 'misc.chal.csaw.io'
TCP_PORT = 9002

# get encrypted flag
def skip():

    # get lines
    r.recvuntil('*', drop=True)
    r.recvuntil('\n', drop=True)

# get new equation
def get_equation():
    data = r.recvuntil('\n', drop=True)
    return data

# connect to server
r = remote(TCP_IP, TCP_PORT)
skip()

def solve_iter():

    # get and edit equation
    equation_string = get_equation()
    if equation_string.find("flag") != -1:
        print "[OK] Flag is: " + equation_string
        exit()
    print "[+] New equation: " + equation_string
    equation_string = equation_string.lower().replace("=", "-")

    # solve
    x = Symbol('x')
    equation = parse_expr(equation_string)
    try:
        solution = solve(equation, x)[0]
    except IndexError:
        print solve(equation, x)
    if str(solution).find("/") != -1:
        solution = Float(solution, 3)
    print "[o] Solution: " + str(solution)

    # send 
    r.send(str(solution) + "\n")
    r.recvuntil('\n', drop=True)

while 1:
    solve_iter()