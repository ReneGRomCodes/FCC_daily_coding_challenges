"""
Circular Prime
Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.

1. is_circular_prime(197) should return True.
2. is_circular_prime(23) should return False.
3. is_circular_prime(13) should return True.
4. is_circular_prime(89) should return False.
5. is_circular_prime(1193) should return True.
"""

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def is_circular_prime(n: int) -> bool:
    s: str = str(n)
    length: int = len(s)

    for i in range(length):
        rotation: int = int(s[i:] + s[:i])

        if not is_prime(rotation):
            return False

    return True


print(is_circular_prime(197))
print(is_circular_prime(23))
print(is_circular_prime(13))
print(is_circular_prime(89))
print(is_circular_prime(1193))
