"""
No Consecutive Repeats
Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.

1. has_no_repeats("hi world") should return True.
2. has_no_repeats("hello world") should return False.
3. has_no_repeats("abcdefghijklmnopqrstuvwxyz") should return True.
4. has_no_repeats("freeCodeCamp") should return False.
5. has_no_repeats("The quick brown fox jumped over the lazy dog.") should return True.
6. has_no_repeats("Mississippi") should return False.
"""

def has_no_repeats(s: str) -> bool:
    for index, char in enumerate(s):
        if index != 0 and s[index] == s[index - 1]:
            return False

    return True


print(has_no_repeats("hi world"))
print(has_no_repeats("hello world"))
print(has_no_repeats("abcdefghijklmnopqrstuvwxyz"))
print(has_no_repeats("freeCodeCamp"))
print(has_no_repeats("The quick brown fox jumped over the lazy dog."))
print(has_no_repeats("Mississippi"))
