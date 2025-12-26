"""
Sum of Divisors
Given a positive integer, return the sum of all its divisors.

A divisor is any integer that divides the number evenly (the remainder is 0).
Only count each divisor once.
For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12.

1. sum_divisors(6) should return 12.
2. sum_divisors(13) should return 14.
3. sum_divisors(28) should return 56.
4. sum_divisors(84) should return 224.
5. sum_divisors(549) should return 806.
6. sum_divisors(9348) should return 23520.
"""

def sum_divisors(n: int) -> int:
    return sum([x for x in range(1, n + 1) if n % x == 0])


print(sum_divisors(6))
print(sum_divisors(13))
print(sum_divisors(28))
print(sum_divisors(84))
print(sum_divisors(549))
print(sum_divisors(9348))
