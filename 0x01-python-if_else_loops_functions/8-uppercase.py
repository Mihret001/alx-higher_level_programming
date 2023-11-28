#!/usr/bin/python3
def uppercase(str):
    for letter in range(str):
        if ord(letter) >= 97 and ord(letter) <= 122:
           x = chr(ord(letter) - 32)
        else:
            x = letter
        print("{}".format(c), end="")
    print()
