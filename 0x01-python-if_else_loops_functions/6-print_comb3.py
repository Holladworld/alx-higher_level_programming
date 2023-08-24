#!/usr/bin/python3
for numbers in range(0, 100):
    digits = numbers % 10
    num = numbers // 10
    if digits > num != num:
        print(":02d}".format(numbers), end="")
        if numbers != 89:
            print(", ", end="")
        else:
            print("\n", end="")
