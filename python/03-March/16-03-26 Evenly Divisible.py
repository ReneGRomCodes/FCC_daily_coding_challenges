"""
Evenly Divisible

Given two integers, determine if you can evenly divide the first one by the second one.

1. is_evenly_divisible(4, 2) should return True.
2. is_evenly_divisible(7, 3) should return False.
3. is_evenly_divisible(5, 10) should return False.
4. is_evenly_divisible(48, 6) should return True.
5. is_evenly_divisible(3186, 9) should return True.
6. is_evenly_divisible(4192, 11) should return False.
"""

def is_evenly_divisible(a: int, b: int) -> bool:
    return a % b == 0


print(is_evenly_divisible(4, 2))
print(is_evenly_divisible(7, 3))
print(is_evenly_divisible(5, 10))
print(is_evenly_divisible(48, 6))
print(is_evenly_divisible(3186, 9))
print(is_evenly_divisible(4192, 11))
