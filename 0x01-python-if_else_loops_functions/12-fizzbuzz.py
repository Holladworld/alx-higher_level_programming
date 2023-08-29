#!/usr/bin/python3
# function that prints the numbers from 1 to 100 separated by a space.
def fizzbuzz():
    for nnum in range(1, 101):
        if nnum % 3 == 0 and nnum % 5 == 0:
            print("FizzBuzz ", end="")
        elif nnum % 3 == 0:
            print("Fizz ", end="")
        elif nnum % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(nnum), end="")
