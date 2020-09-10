#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, (int, float)) or not roman_string:
        return 0
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = i = 0
    _len = len(roman_string)
    while i < _len:
        if (i < _len - 1 and roman_string[i] == 'I' and
                roman_string[i+1] in "VX"):
            n += r[roman_string[i+1]] - 1
            i += 2
        elif (i < _len - 1 and roman_string[i] == 'X' and
              roman_string[i+1] in "C"):
            n += r[roman_string[i+1]] - 10
            i += 2
        elif (i < _len - 1 and roman_string[i] == 'C' and
              roman_string[i+1] in "M"):
            n += r[roman_string[i+1]] - 100
            i += 2
        else:
            n += r[roman_string[i]]
            i += 1
    return n
