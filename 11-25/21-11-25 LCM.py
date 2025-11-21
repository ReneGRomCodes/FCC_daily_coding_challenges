"""
LCM
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6,
return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multiplies of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.

1. lcm(4, 6) should return 12.
2. lcm(9, 6) should return 18.
3. lcm(10, 100) should return 100.
4. lcm(13, 17) should return 221.
5. lcm(45, 70) should return 630.
"""

def lcm(a: int, b: int) -> int:
    multiplier: int = 1
    n_1, n_2 = max(a, b), min(a, b)

    while True:
        multiple: int = n_1 * multiplier

        if multiple % n_2 == 0:
            return multiple

        multiplier += 1


print(lcm(4, 6))
print(lcm(9, 6))
print(lcm(10, 100))
print(lcm(13, 17))
print(lcm(45, 70))
