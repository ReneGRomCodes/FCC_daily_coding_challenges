"""
Parsec Converter
In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its
equivalent in time or distance.

- If the given integer is odd, it represents time. If it's even, it represents distance.

Use these conversion rates:
Parsecs	Time/Distance
1	    2 hours
2	    6 light years

Return the converted value as an integer.

1. convert_parsecs(1) should return 2.
2. convert_parsecs(2) should return 6.
3. convert_parsecs(31) should return 62.
4. convert_parsecs(88) should return 264.
5. convert_parsecs(17) should return 34.
6. convert_parsecs(14) should return 42.
"""

def convert_parsecs(parsecs):
    is_time: bool = parsecs % 2 != 0

    if is_time:
        return parsecs * 2
    else:
        return parsecs * 3


print(convert_parsecs(1))
print(convert_parsecs(2))
print(convert_parsecs(31))
print(convert_parsecs(88))
print(convert_parsecs(17))
print(convert_parsecs(14))
