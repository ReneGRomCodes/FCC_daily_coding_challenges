"""
Duplicate Character Count
Given two strings, return a count of characters from the second string that can be found in the first.

- Duplicate characters in the second string are counted separately.

1. duplicateCharacterCount("aloha", "hei") should return 1.
2. duplicateCharacterCount("jambo", "bonjour") should return 4.
3. duplicateCharacterCount("hello", "hola") should return 3.
4. duplicateCharacterCount("ola", "hej") should return 0.
5. duplicateCharacterCount("ciao", "konnichiwa") should return 5.
6. duplicateCharacterCount("merhaba", "xin chao") should return 2.
7. duplicateCharacterCount("hello world", "hello to everyone around the world") should return 26.
"""

def duplicate_character_count(str1: str, str2: str) -> int:
    counter: int = 0

    for char in str2:
        if char in str1:
            counter += 1

    return counter


print(duplicate_character_count("aloha", "hei"))
print(duplicate_character_count("jambo", "bonjour"))
print(duplicate_character_count("hello", "hola"))
print(duplicate_character_count("ola", "hej"))
print(duplicate_character_count("ciao", "konnichiwa"))
print(duplicate_character_count("merhaba", "xin chao"))
print(duplicate_character_count("hello world", "hello to everyone around the world"))
