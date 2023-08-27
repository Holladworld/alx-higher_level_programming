#!/usr/bin/python3
def uppercase(str):
    for letters in str:
        if ord('a') <= ord(letters) <= ord('z'):
            letters = chr(ord(letters) - 32)
        print("{}".format(letters), end="")
    print()
