"""
Word Score

Given a word, return its score using a standard letter-value table:
Letter	Value
     A      1
     B      2
   ...    ...
     Z     26

Upper and lowercase letters have the same value.

1. get_word_score("hi") should return 17.
2. get_word_score("hello") should return 52.
3. get_word_score("hippopotamus") should return 169.
4. get_word_score("freeCodeCamp") should return 94.
"""

def get_word_score(word: str) -> int:
    value = 0

    for char in word.lower():
        value += ord(char) - 96

    return value


print(get_word_score("hi"))
print(get_word_score("hello"))
print(get_word_score("hippopotamus"))
print(get_word_score("freeCodeCamp"))
