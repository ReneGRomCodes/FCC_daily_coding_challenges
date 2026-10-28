"""
Sum the Letters
Given a string, return the sum of its letters.

Letters are A-Z in uppercase or lowercase
Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
Uppercase and lowercase letters have the same value.
Ignore all non-letter characters.

1. sum_letters("Hello") should return 52.
2. sum_letters("freeCodeCamp") should return 94.
3. sum_letters("The quick brown fox jumps over the lazy dog.") should return 473.
4. sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit,
    facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.") should return 1681.
5. sum_letters("</404>") should return 0.
"""

def sum_letters(s: str) -> int:
    letters_sum: int = 0

    for char in s:
        if char.isalpha():
            letters_sum += ord(char.upper()) - 64

    return letters_sum


print(sum_letters("Hello"))
print(sum_letters("freeCodeCamp"))
print(sum_letters("The quick brown fox jumps over the lazy dog."))
print(sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, "
                  "facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci."))
print(sum_letters("</404>"))
