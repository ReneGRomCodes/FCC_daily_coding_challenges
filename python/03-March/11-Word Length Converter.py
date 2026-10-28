"""
Word Length Converter
Given a string of words, return a new string where each word is replaced by its length.

Words in the given string will be separated by a single space
Keep the spaces in the returned string.
For example, given "hello world", return "5 5".

1. convert_words("hello world") should return "5 5".
2. convert_words("Thanks and happy coding") should return "6 3 5 6".
3. convert_words("The quick brown fox jumps over the lazy dog") should return "3 5 5 3 5 4 3 4 3".
4. convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl")
    should return "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4".
"""

def convert_words(s: str) -> str:
    word_lengths: list[str] = [str(len(x)) for x in s.split()]

    return " ".join(word_lengths)


print(convert_words("hello world"))
print(convert_words("Thanks and happy coding"))
print(convert_words("The quick brown fox jumps over the lazy dog"))
print(convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl"))
