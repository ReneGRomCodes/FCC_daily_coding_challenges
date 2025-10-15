"""
String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the
second two.

1. count('abcdefg', 'def') should return 1.
2. count('hello', 'world') should return 0.
3. count('mississippi', 'iss') should return 2.
4. count('she sells seashells by the seashore', 'sh') should return 3.
5. count('101010101010101010101', '101') should return 10.
"""

def count(text: str, parameter: str) -> int:
    counter: int = 0

    for index, _ in enumerate(text):
        if text[index:index+len(parameter)] == parameter:
            counter += 1

    return counter


print(count('abcdefg', 'def'))
print(count('hello', 'world'))
print(count('mississippi', 'iss'))
print(count('she sells seashells by the seashore', 'sh'))
print(count('101010101010101010101', '101'))
