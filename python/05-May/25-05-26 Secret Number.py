"""
Secret Number
Given a secret number and a guess, determine if the guess is correct.

Return:
- "higher" if the secret number is higher than the guess.
- "lower" if the secret number is lower than the guess.
- "you got it!" if the guess is correct.

1. guess_number(50, 30) should return "higher".
2. guess_number(85, 99) should return "lower".
3. guess_number(2026, 2026) should return "you got it!".
4. guess_number(92904, 11283) should return "higher".
5. guess_number(230495, 423920) should return "lower".
6. guess_number(120349, 120349) should return "you got it!".
"""

def guess_number(secret: int, guess: int) -> str:
    if guess < secret:
        return "higher"
    elif guess > secret:
        return "lower"
    elif guess == secret:
        return "you got it!"

    return "How the hell did that happen?!"


print(guess_number(50, 30))
print(guess_number(85, 99))
print(guess_number(2026, 2026))
print(guess_number(92904, 11283))
print(guess_number(230495, 423920))
print(guess_number(120349, 120349))
