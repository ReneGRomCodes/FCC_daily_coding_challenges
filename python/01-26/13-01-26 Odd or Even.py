"""
Odd or Even?
Given a positive integer, return "Odd" if it's an odd number, and "Even" is it's even.

1. odd_or_even(1) should return "Odd".
2. odd_or_even(2) should return "Even".
3. odd_or_even(13) should return "Odd".
4. odd_or_even(196) should return "Even".
5. odd_or_even(123456789) should return "Odd".
"""

def odd_or_even(n: int) -> str:
    if n % 2:
        return "Odd"

    return "Even"


print(odd_or_even(1))
print(odd_or_even(2))
print(odd_or_even(13))
print(odd_or_even(196))
print(odd_or_even(123456789))
