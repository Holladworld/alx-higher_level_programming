#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = ("Last digit of ")

if number < 0:
    last_digit_of = number % -10
elif number >= 0:
    last_digit_of = number % 10
if last_digit_of > 5:
    print("{}{} is {} and is greater than 5".format(i, number, last_digit_of))
elif last_digit_of == 0:
    print("{}{} is {} and is 0".format(i, number, last_digit_of))
else:
    print("{}{} is {} and is less than 6 and not 0".format(i, number, last_digit_of))
