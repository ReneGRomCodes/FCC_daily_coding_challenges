"""
Digits vs Letters
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than
digits, and "tie" if it has the same amount of digits and letters.

Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters.

1. digits_or_letters("abc123") should return "tie".
2. digits_or_letters("a1b2c3d") should return "letters".
3. digits_or_letters("1a2b3c4") should return "digits".
4. digits_or_letters("abc123!@#DEF") should return "letters".
5. digits_or_letters("H3110 W0R1D") should return "digits".
6. digits_or_letters("P455W0RD") should return "tie".
"""

def digits_or_letters(s: str) -> str:
    n_digits: int = len([char for char in s if char.isnumeric()])
    n_letters: int = len([char for char in s if char.isalpha()])

    if n_digits > n_letters:
        return "digits"
    elif n_digits < n_letters:
        return "letters"

    return "tie"


print(digits_or_letters("abc123"))
print(digits_or_letters("a1b2c3d"))
print(digits_or_letters("1a2b3c4"))
print(digits_or_letters("abc123!@#DEF"))
print(digits_or_letters("H3110 W0R1D"))
print(digits_or_letters("P455W0RD"))
