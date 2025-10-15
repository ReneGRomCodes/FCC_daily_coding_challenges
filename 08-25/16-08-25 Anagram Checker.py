"""
Anagram Checker
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

Ignore casing and white space.

1. are_anagrams("listen", "silent") should return true.
2. are_anagrams("School master", "The classroom") should return true.
3. are_anagrams("A gentleman", "Elegant man") should return true.
4. are_anagrams("Hello", "World") should return false.
5. are_anagrams("apple", "banana") should return false.
6. are_anagrams("cat", "dog") should return false.
"""

def are_anagrams(str1: str, str2: str) -> bool:
    processed_str1: list[str] = sorted(str1.lower().replace(" ", ""))
    processed_str2: list[str] = sorted(str2.lower().replace(" ", ""))

    return processed_str1 == processed_str2


print(are_anagrams("listen", "silent"))
print(are_anagrams("School master", "The classroom"))
print(are_anagrams("A gentleman", "Elegant man"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("apple", "banana"))
print(are_anagrams("cat", "dog"))
