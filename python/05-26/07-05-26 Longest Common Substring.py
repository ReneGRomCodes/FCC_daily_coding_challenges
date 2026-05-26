"""
Longest Common Substring
Given a string, return the longest substring that appears more than once.

- The substrings can overlap.

1. get_longest_substring("abracadabra") should return "abra".
2. get_longest_substring("hello world hello") should return "hello".
3. get_longest_substring("mississippi") should return "issi".
4. get_longest_substring("ha ha ha ha ha ha ha") should return "ha ha ha ha ha ha".
5. get_longest_substring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over")
    should return "the quick brown fox jumped over".
"""


def get_longest_substring(s: str) -> str:
    max_window_size: int = len(s) - 1

    for size in range(max_window_size, 0, -1):

        for start in range(len(s) - size + 1):
            window = s[start: start + size]

            if window in s[start + 1:]:
                return window

    return ""

print(get_longest_substring("abracadabra"))
print(get_longest_substring("hello world hello"))
print(get_longest_substring("mississippi"))
print(get_longest_substring("ha ha ha ha ha ha ha"))
print(get_longest_substring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over"))
