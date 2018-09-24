# import some libraries
import string

# set some constants
setups = [[1, 0, 0], [1, 1, 0], [0, 1, 1], [0, 0, 1]]

# Stackoverflow <3
def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

# open ping file
pings = open("ping_3.txt", "r")
content = pings.read()
lines = string.split(content, '\n')
for pair in setups:
    bits = ""
    under_200 = pair[0]
    under_800 = pair[1] 
    above_1000 = pair[2]
    for line in lines:
        time = float(find_between(line, "time=", " ms"))
        if time < 200:
            # bits = bits + str(under_200)
            continue
        if time < 800:
            bits = bits + str(under_800)
            continue
        if time > 1000:
            bits = bits + str(above_1000)
            continue
    if ((under_200, under_800, above_1000) == (0, 0, 1)):
        print "[+] Bits for setup " + str((under_200, under_800, above_1000)) +  " are: " + bits
    else: 
        print "[-] Bits for setup " + str((under_200, under_800, above_1000)) +  " are: " + bits