"""
Unnatural Prime
Given an integer, determine if that number is a prime number or a negative prime number.

A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
A negative prime number is the negative version of a positive prime number.
1 and 0 are not considered prime numbers.

1. is_unnatural_prime(1) should return False.
2. is_unnatural_prime(-1) should return False.
3. is_unnatural_prime(19) should return True.
4. is_unnatural_prime(-23) should return True.
5. is_unnatural_prime(0) should return False.
6. is_unnatural_prime(97) should return True.
7. is_unnatural_prime(-61) should return True.
8. is_unnatural_prime(99) should return False.
9. is_unnatural_prime(-44) should return False.
"""

def is_unnatural_prime(n: int) -> bool:
    abs_n = abs(n)

    if abs_n < 2:
        return False

    for i in range(2, (abs_n // 2) + 1):
        if abs_n % i == 0:
            return False

    return True


print(is_unnatural_prime(1))
print(is_unnatural_prime(-1))
print(is_unnatural_prime(19))
print(is_unnatural_prime(-23))
print(is_unnatural_prime(0))
print(is_unnatural_prime(97))
print(is_unnatural_prime(-61))
print(is_unnatural_prime(99))
print(is_unnatural_prime(-44))
