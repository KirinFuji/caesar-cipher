
# Written by https://github.com/KirinFuji

import sys, getopt, re

ENG_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
               #01234567891111111111222222
               #          0123456789012345 

def getInt(char, alphabet):
    return re.search(f"{char}", alphabet).start()

def increment(char, ammount, alphabet, bounds):
    char = char.upper()
    if char in alphabet:
        v = getInt(char, alphabet)    
        for i in range(0,ammount):
            if v < bounds - 1:
                v += 1
            else:
                v = 0
        return alphabet[v]

def decrement(char, ammount, alphabet, bounds):
    char = char.upper()
    if char in alphabet:
        v = getInt(char, alphabet)    
        for i in range(0,ammount):
            if v > 0:
                v -= 1
            else:
                v = bounds - 1
        return alphabet[v]

def c_cipher(cleartext, rotation_ammount):
    string = ""
    for char in cleartext:
        if re.match(r"\w", char):
            char = increment(char, rotation_ammount, ENG_ALPHABET, 26)
            string = string + char
        if re.match(r"\s", char):
            string = string + char
    return(string)

def c_decipher(ciphertext, rotation_ammount):
    string = ""
    for char in ciphertext:
        if re.match(r"\w", char):
            char = decrement(char, rotation_ammount, ENG_ALPHABET, 26)
            string = string + char
        if re.match(r"\s", char):
            string = string + char
    return(string)

"""--------------------------------"""
"""      CMD Line Input            """
"""--------------------------------"""


def main(argv):
    method = "encode"
    inputtext = "Hello World"
    rot_ammount = 13
    try:
        opts, args = getopt.getopt(argv,"hdet:r:",["text=","rot="])
    except getopt.GetoptError:
        print('caesar-cipher.py (-e for encode -d for decode) -t <input text> -r <rotation ammount>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('caesar-cipher.py (-e for encode -d for decode) -t <input text> -r <rotation ammount>')
            sys.exit(101)
        elif opt == '-e':
            method = "encode"
        elif opt == '-d':
            method = "decode"
        elif opt in ("-t", "--text"):
            inputtext = arg
        elif opt in ("-r", "--rot"):
            try:
                rot_ammount = int(arg)
            except:
                print("Invalid input type for rotation ammount.")
                sys.exit()

    if method == "encode":
        print(c_cipher(inputtext, rot_ammount))
    elif method == "decode":
        print(c_decipher(inputtext, rot_ammount))


if __name__ == "__main__":
   main(sys.argv[1:])
