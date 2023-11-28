#!/usr/bin/python3
def uppercase(str):
    for letter in (str):
        if ord(letter) >= 97 and ord(letter) <= 122:
            x = chr(ord(letter) - 32)
        else:
            x = letter
        print("{}".format(x), end="")
    print()
