"""
Roman Numeral Parser
Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol	Value
I	    1
V	    5
X	    10
L	    50
C	    100
D	    500
M	    1000

Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise,
values are added.

1. parse_roman_numeral("III") should return 3.
2. parse_roman_numeral("IV") should return 4.
3. parse_roman_numeral("XXVI") should return 26.
4. parse_roman_numeral("XCIX") should return 99.
5. parse_roman_numeral("CDLX") should return 460.
6. parse_roman_numeral("DIV") should return 504.
7. parse_roman_numeral("MMXXV") should return 2025.
"""

def convert_single_numeral(single_numeral: str) -> int:
    conversion_table: dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    return conversion_table[single_numeral]


def parse_roman_numeral(numeral: str) -> int:
    converted_numerals: list[int] = [convert_single_numeral(x) for x in numeral]
    sum_n: int = 0

    for i in range(len(converted_numerals) - 1):
        if converted_numerals[i] < converted_numerals[i + 1]:
            sum_n -= converted_numerals[i]
        else:
            sum_n += converted_numerals[i]

    sum_n += converted_numerals[-1]

    return sum_n


print(parse_roman_numeral("III"))
print(parse_roman_numeral("IV"))
print(parse_roman_numeral("XXVI"))
print(parse_roman_numeral("XCIX"))
print(parse_roman_numeral("CDLX"))
print(parse_roman_numeral("DIV"))
print(parse_roman_numeral("MMXXV"))
