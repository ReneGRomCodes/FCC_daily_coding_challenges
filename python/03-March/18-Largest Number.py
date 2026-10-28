"""
Largest Number
Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").

1. largest_number("1,2") should return 2.
2. largest_number("4;15:60,26?52!0") should return 60.
3. largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011") should return -402.
4. largest_number("12;-50,99.9,49.1!-10.1?88?16") should return 99.9.
"""

def largest_number(s: str) -> int | float:
    for separator in (",", "!", "?", ":", ";"):
        s = s.replace(separator, " ")

    max_n = max([float(n) for n in s.split()])

    if max_n % 1 == 0:
        return int(max_n)
    else:
        return max_n


print(largest_number("1,2"))
print(largest_number("4;15:60,26?52!0"))
print(largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011"))
print(largest_number("12;-50,99.9,49.1!-10.1?88?16"))
