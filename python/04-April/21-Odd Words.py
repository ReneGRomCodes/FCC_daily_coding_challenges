"""
Odd Words
Given a string of words, return only the words with an odd number of letters.

- Words in the given string will be separated by a single space.
- Return the words separated by a single space.

1. get_odd_words("This is a super good test") should return "a super".
2. get_odd_words("one two three four") should return "one two three".
3. get_odd_words("banana split sundae with rainbow sprinkles on top") should return "split rainbow sprinkles top".
4. get_odd_words("The quick brown fox jumped over the lazy river") should return "The quick brown fox the river".
"""

def get_odd_words(s: str) -> str:
    return " ".join([word for word in s.split(" ") if len(word) % 2 != 0])


print(get_odd_words("This is a super good test"))
print(get_odd_words("one two three four"))
print(get_odd_words("banana split sundae with rainbow sprinkles on top"))
print(get_odd_words("The quick brown fox jumped over the lazy river"))
