"""
Number Words
Given an integer from 0 to 99, return its English word representation.

- 0 returns "zero".
- Numbers 1-19 have unique names ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
- Multiples of 10 from 20-90 have their own names ("twenty", "thirty", ..., "eighty", "ninety").
- Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example "forty-two" and
  "fifty-three".

1. getNumberWords(0) should return "zero".
2. getNumberWords(10) should return "ten".
3. getNumberWords(19) should return "nineteen".
4. getNumberWords(30) should return "thirty".
5. getNumberWords(53) should return "fifty-three".
6. getNumberWords(7) should return "seven".
7. getNumberWords(12) should return "twelve".
8. getNumberWords(60) should return "sixty".
9. getNumberWords(67) should return "sixty-seven".
10. getNumberWords(98) should return "ninety-eight".
"""

def get_number_words(n: int) -> str:
    number_words: dict[int, str] = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if n <= 19 or n % 10 == 0:
        return number_words[n]
    else:
        n_arr: list[int] = [int(n) for n in str(n)]
        return f"{number_words[n_arr[0] * 10]}-{number_words[n_arr[1]]}"


print(get_number_words(0))
print(get_number_words(10))
print(get_number_words(19))
print(get_number_words(30))
print(get_number_words(53))
print(get_number_words(7))
print(get_number_words(12))
print(get_number_words(60))
print(get_number_words(67))
print(get_number_words(98))
