"""
Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

- A palindrome is a string that is the same forward and backward.
- If it's not a palindrome, return "none".

1. palindrome_locator("racecar") should return "e".
2. palindrome_locator("level") should return "v".
3. palindrome_locator("freecodecamp") should return "none".
4. palindrome_locator("noon") should return "oo".
5. palindrome_locator("11100111") should return "00".
"""

def palindrome_locator(s: str) -> str:
    if not s == s[::-1]:
        return "none"

    s_length: int = len(s)
    center_index: int = int(s_length / 2)

    if s_length % 2 == 0:
        return s[center_index - 1:center_index + 1]
    else:
        return s[center_index]


print(palindrome_locator("racecar"))
print(palindrome_locator("level"))
print(palindrome_locator("freecodecamp"))
print(palindrome_locator("noon"))
print(palindrome_locator("11100111"))
