#!/usr/bin/python3
for letters in range(97, 123):
    if letters != 101 and letters != 113:
        print("{:s}".format(chr(letters)), end="")
