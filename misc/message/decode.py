# define some staff
FLAG_START = "DCTF{"
FLAG_END = "}"

# Stackoverflow, my love
def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
def check_type(string):
    try:
        bullshit = str(int(string))
        return "int"
    except ValueError:
        return "string"

# get content
encoded = open("message.txt", "r")
content = encoded.read()
encoded.close()

# replace
flag = ""
sha = find_between(content, "{", "}").replace('qwerty', ' ').replace('asdfgh', ' ').replace('zxcvbn', ' ')
array = sha.split()
print "[+] Your flag content is: " + sha
for elem in array:
    if check_type(elem) == "int":
        print "[+] New character found: " + elem
        flag = flag + str(elem)
    else:
        print "[+] New combo found, please enter in browser page: " + elem
        letter = raw_input('Enter the letter: ')
        flag = flag + letter
print "[+] Your flag content is: " + FLAG_START + flag + FLAG_END