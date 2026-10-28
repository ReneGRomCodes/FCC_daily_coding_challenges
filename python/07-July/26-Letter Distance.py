"""
Letter Distance
Given two strings of equal length, return the sum of the shortest distances between each pair of characters.

- The input will only contain lowercase letters
- The alphabet is treated as a circle, so the distance between a and z is 1.

1. letter_distance("abc", "bcd") should return 3.
2. letter_distance("abc", "xyz") should return 9.
3. letter_distance("encrypt", "decrypt") should return 10.
4. letter_distance("algorithm", "codeblock") should return 43.
5. letter_distance("lobster", "penguin") should return 47.
6. letter_distance("alligator", "crocodile") should return 55.
"""

def letter_distance(str1: str, str2: str) -> int:
    distance: int = 0

    for char1, char2 in zip(str1, str2):
        diff = abs(ord(char1) - ord(char2))
        distance += min(diff, 26 - diff)

    return distance


print(letter_distance("abc", "bcd"))
print(letter_distance("abc", "xyz"))
print(letter_distance("encrypt", "decrypt"))
print(letter_distance("algorithm", "codeblock"))
print(letter_distance("lobster", "penguin"))
print(letter_distance("alligator", "crocodile"))
