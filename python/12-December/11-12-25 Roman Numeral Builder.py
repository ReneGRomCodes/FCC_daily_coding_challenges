"""
Roman Numeral Builder
Given an integer, return its equivalent value in Roman numerals.

Roman numerals use these symbols:

Symbol	Value
I	    1
V	    5
X	    10
L	    50
C	    100
D	    500
M	    1000

Roman numerals are written from largest to smallest, left to right using the following rules:

Addition is used when a symbol is followed by one of equal or smaller value. For example, 18 is written as XVIII
(10 + 5 + 1 + 1 + 1 = 18).
Subtraction is used when a smaller symbol appears before a larger one, to represent 4 or 9 in any place value. For
example, 19 is written as XIX (10 + (10 - 1)).
No symbol may be repeated more than three times in a row. Subtraction is used when you would otherwise need to write a
symbol more than three times in a row. So the largest number you can write is 3999.
Here's one more example: given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1)).

1. to_roman(18) should return "XVIII".
2. to_roman(19) should return "XIX".
3. to_roman(1464) should return "MCDLXIV".
4. to_roman(2025) should return "MMXXV".
5. to_roman(3999) should return "MMMCMXCIX".
"""


def to_roman(num: int) -> str:
    roman_map: list[tuple[int, str]] = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result: list[str] = []

    for value, symbol in roman_map:
        while num >= value:
            result.append(symbol)
            num -= value

    return "".join(result)


print(to_roman(18))
print(to_roman(19))
print(to_roman(1464))
print(to_roman(2025))
print(to_roman(3999))
