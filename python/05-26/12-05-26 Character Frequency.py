"""
Character Frequency
Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it
appears.

1. get_frequency("test") should return {"t": 2, "e": 1, "s": 1}.
2. get_frequency("mississippi") should return {"m": 1, "i": 4, "s": 4, "p": 2}.
3. get_frequency("hello world") should return {"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1}.
4. get_frequency("She sells seashells by the seashore.")
    should return {"S": 1, "h": 4, "e": 7, " ": 5, "s": 7, "l": 4, "a": 2, "b": 1, "y": 1, "t": 1, "o": 1, "r": 1, ".": 1}.
5. get_frequency("The quick brown fox jumps over the lazy dog.")
    should return {"T": 1, "h": 2, "e": 3, " ": 8, "q": 1, "u": 2, "i": 1, "c": 1, "k": 1, "b": 1, "r": 2, "o": 4,
    "w": 1, "n": 1, "f": 1, "x": 1, "j": 1, "m": 1, "p": 1, "s": 1, "v": 1, "t": 1, "l": 1, "a": 1, "z": 1, "y": 1,
    "d": 1, "g": 1, ".": 1}.
"""

def get_frequency(s):
    histogram: dict[str, int] = {}

    for char in s:
        if char not in histogram:
            histogram[char] = s.count(char)

    return histogram


print(get_frequency("test"))
print(get_frequency("mississippi"))
print(get_frequency("hello world"))
print(get_frequency("She sells seashells by the seashore."))
print(get_frequency("The quick brown fox jumps over the lazy dog."))
