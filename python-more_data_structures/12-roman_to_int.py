#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str and roman_string is not None:
        return 0
    roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    result = 0
    i = 0
    while i < len(roman_string):
        value = roman[roman_string[i]]
        if i < len(roman_string) - 1 and value < roman[roman_string[i + 1]]:
            result = roman[roman_string[i + 1]] - value
            i += 1
        else:
            result += value
        i += 1
    return result
