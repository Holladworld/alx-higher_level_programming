#!/usr/bin/python3
# program that imports functions from the file
# calculator_1.py, does some Maths, and prints the result.

if __name__ == '__main__':
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
