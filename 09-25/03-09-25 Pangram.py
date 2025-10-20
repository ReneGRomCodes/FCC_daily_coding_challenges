"""
Pangram
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from
the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.

1. is_pangram("hello", "helo") should return True
2. is_pangram("hello", "hel") should return False
3. is_pangram("hello", "helow") should return False
4. is_pangram("hello world", "helowrd") should return True
5. is_pangram("Hello World!", "helowrd") should return True
6. is_pangram("Hello World!", "heliowrd") should return False
7. is_pangram("freeCodeCamp", "frcdmp") should return False
8. is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") should return True
"""

def is_pangram(sentence: str, letters: str) -> bool:
    sentence_set: set[str] = {c for c in sentence.lower() if c.isalpha()}
    letters_set: set[str] = set(letters)

    if sentence_set == letters_set:
        return True

    return False


print(is_pangram("hello", "helo"))
print(is_pangram("hello", "hel"))
print(is_pangram("hello", "helow"))
print(is_pangram("hello world", "helowrd"))
print(is_pangram("hello world!", "helowrd"))
print(is_pangram("hello world!", "heliowrd"))
print(is_pangram("freeCodeCamp", "frcdmp"))
print(is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"))
