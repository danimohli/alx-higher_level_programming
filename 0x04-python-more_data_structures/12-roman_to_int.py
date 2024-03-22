#!/usr/bin/python3

# convert roman numeral to integer
def roman_to_int(roman_string):

    # checking if incoming arg is str
    if isinstance(roman_string, int) or roman_string is None:
        return 0
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}

    tal = 0
    value = 0

    for x in roman_string[::-1]:
        va = numerals[x]
        if va < value:
            tal -= va
        else:
            tal += va
        value = va

    return tal
