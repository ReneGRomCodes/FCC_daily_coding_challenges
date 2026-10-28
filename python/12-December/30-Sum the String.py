"""
Sum the String
Given a string containing digits and other characters, return the sum of all numbers in the string.

Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
Ignore any non-digit characters.

1. string_sum("3apples2bananas") should return 5.
2. string_sum("10cats5dogs2birds") should return 17.
3. string_sum("125344") should return 125344.
4. string_sum("a1b20c300") should return 321.
5. string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5") should return 1653.
"""

def string_sum(s: str) -> int:
    extracted_s: str = "".join(char if char.isnumeric() else " " for char in s)

    return sum([int(x) for x in extracted_s.split()])


print(string_sum("3apples2bananas"))
print(string_sum("10cats5dogs2birds"))
print(string_sum("125344"))
print(string_sum("a1b20c300"))
print(string_sum("a12b34c56d78e90f123g456h789i0j1k2l3m4n5"))
