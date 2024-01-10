#!/usr/bin/python3
def roman_dict(char):
    if char ==  'I':
        return 1
    if char == 'V':
        return 5
    if char == 'X':
        return 10
    if char == 'L':
        return 50
    if char == 'C':
        return 100
    if char == 'D':
        return 500
    if char == 'M':
        return 1000
    return -1

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return (0)
    result = 0

    for i in range(len(roman_string) - 1):
        if i < (len(roman_string)) and roman_dict(roman_string[i]) < roman_dict(roman_string[i + 1]):
                result -= roman_dict(roman_string[i])
        else:
            result += roman_dict(roman_string[i])
    result += roman_dict(roman_string[-1])
    return (result)
