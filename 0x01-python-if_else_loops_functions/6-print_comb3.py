#!/usr/bin/python3
for numbers in range(0, 10):
    for digit in range(numbers + 1, 10):
        if numbers == 8 and digit == 9:
            print('89')
        else:
            print('{}{}, '.format(numbers, digit), end='')
