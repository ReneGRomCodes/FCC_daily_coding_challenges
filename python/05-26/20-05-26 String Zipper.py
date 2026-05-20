"""
String Zipper
Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append
the remaining characters at the end.

Begin with the first character of the first string.

1. zip_strings("abc", "123") should return "a1b2c3".
2. zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz") should return "abcdefghijklmnopqrstuvwxyz".
3. zip_strings("day", "night") should return "dnaiyght".
4. zip_strings("python", "javascript") should return "pjyatvhaosncript".
5. zip_strings("feCdCm", "reoeap") should return "freeCodeCamp".
"""

def zip_strings(a: str, b: str) -> str:
    zipped = ""
    min_length = min(len(a), len(b))

    # Zip both strings. Will stop at the end of the shorter string.
    for char_1, char_2 in zip(a, b):
        zipped += char_1 + char_2

    # Add the 'leftover' of the longer string. The slice of the shorter string will be empty.
    zipped += a[min_length:] + b[min_length:]

    return zipped


print(zip_strings("abc", "123"))
print(zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz"))
print(zip_strings("day", "night"))
print(zip_strings("python", "javascript"))
print(zip_strings("feCdCm", "reoeap"))
