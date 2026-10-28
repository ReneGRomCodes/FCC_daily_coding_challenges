"""
Smallest Gap
Given a string, return the substring between the two identical characters that have the smallest number of characters
between them (smallest gap).

There will always be at least one pair of matching characters.
The returned substring should exclude the matching characters.
If two or more gaps are the same length, return the characters from the first one.
For example, given "ABCDAC", return "DA".

Only "A" and "C" repeat in the string.
The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
So return the string between the two "C" characters.

1. smallest_gap("ABCDAC") should return "DA".
2. smallest_gap("racecar") should return "e".
3. smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4") should return "#q6e&rkf(p".
4. smallest_gap("Hello World") should return "".
5. smallest_gap("The quick brown fox jumps over the lazy dog.") should return "fox".
"""

def smallest_gap(s: str) -> str:
    last_seen: dict[str, int] = {}
    min_gap: float = float("inf")
    result: str = ""

    for i, ch in enumerate(s):
        if ch in last_seen:
            gap = i - last_seen[ch] - 1

            if gap < min_gap:
                min_gap = gap
                result = s[last_seen[ch] + 1:i]

        last_seen[ch] = i

    return result


print(smallest_gap("ABCDAC"))
print(smallest_gap("racecar"))
print(smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"))
print(smallest_gap("Hello World"))
print(smallest_gap("The quick brown fox jumps over the lazy dog."))
