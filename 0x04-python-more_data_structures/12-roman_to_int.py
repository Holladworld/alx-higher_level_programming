#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict =  {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sumTotal = 0
    for roman_num in reversed(roman_string):
        roman = roman_dict[roman_num]
        sumTotal += roman if sumTotal < roman * 5 else -roman

    if not roman_string or type(roman_string) != str:
            return 0
    return sumTotal
