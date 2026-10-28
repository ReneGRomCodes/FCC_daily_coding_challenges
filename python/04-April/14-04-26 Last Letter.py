"""
Last Letter
Given a string, return the letter from the string that appears last in the alphabet.

- If two or more letters tie for the last in the alphabet, return the first one.
- Ignore all non-letter characters.

1. get_last_letter("world") should return "w".
2. get_last_letter("Hello World") should return "W".
3. get_last_letter("The quick brown fox jumped over the lazy dog.") should return "z".
4. get_last_letter("HeLl0") should return "L".
5. get_last_letter("!#$ er@R asd fT.,> 2t0e9") should return "T".
"""

def get_last_letter(s: str) -> str:
    max_char: str = max([x.lower() for x in s if x.isalpha()])
    max_char_index: int = s.lower().index(max_char)

    return s[max_char_index]


def unreadable_get_last_letter(s: str) -> str:
    """Solution above squeezed into a one-liner... because why not? ;)"""
    return s[s.lower().index(max([x.lower() for x in s if x.isalpha()]))]


print(get_last_letter("world"))
print(get_last_letter("Hello World"))
print(get_last_letter("The quick brown fox jumped over the lazy dog."))
print(get_last_letter("HeLl0"))
print(get_last_letter("!#$ er@R asd fT.,> 2t0e9"))
