"""
Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".

1. count_permutations("abb") should return 3.
2. count_permutations("abc") should return 6.
3. count_permutations("racecar") should return 630.
4. count_permutations("freecodecamp") should return 39916800.
"""

def count_permutations(s: str) -> int:
    # Simple factorial.
    def factorial(n):
        r = 1
        for i in range(2, n+1):
            r *= i
        return r

    # Frequency count.
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    total = factorial(len(s))
    for v in frequency.values():
        total //= factorial(v)

    return total


print(count_permutations("abb"))
print(count_permutations("abc"))
print(count_permutations("racecar"))
print(count_permutations("freecodecamp"))
