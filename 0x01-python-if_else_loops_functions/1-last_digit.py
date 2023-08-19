#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit_of = number % 10
else:
    last_digit_of = (-1* number % 10) * -1
    message = "Last digit of {} is {}".format(number, last_digit_of, last_digit_of)
    if last_digit_of > 5:
        print(message, "and is greate than 5")
    elif last_digit_of < 5 and last_digit_of != 0:
        print(message, "and is less than 6 and not 0")
    else:
        print(message, "and is 0")

