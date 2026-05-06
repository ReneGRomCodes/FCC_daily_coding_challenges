"""
Narcissistic Number
Given a positive integer, determine whether it is a narcissistic number.

- A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the
number itself.

For example, 153 has 3 digits, and 1**3 + 5**3 + 3**3 = 153, so it is narcissistic.

1. is_narcissistic(153) should return True.
2. is_narcissistic(154) should return False.
3. is_narcissistic(371) should return True.
4. is_narcissistic(512) should return False.
5. is_narcissistic(9) should return True.
6. is_narcissistic(11) should return False.
7. is_narcissistic(9474) should return True.
8. is_narcissistic(6549) should return False.
"""

def is_narcissistic(n: int) -> bool:
    s: str = str(n)
    power: int = len(s)
    checksum: int = 0

    for i in range(power):
        checksum += int(s[i]) ** power

    return n == checksum


print(is_narcissistic(153))
print(is_narcissistic(154))
print(is_narcissistic(371))
print(is_narcissistic(512))
print(is_narcissistic(9))
print(is_narcissistic(11))
print(is_narcissistic(9474))
print(is_narcissistic(6549))
