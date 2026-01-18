"""
Perfect Square
Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect
square because you can multiply 3 by itself to get it.

1. is_perfect_square(9) should return True.
2. is_perfect_square(49) should return True.
3. is_perfect_square(1) should return True.
4. is_perfect_square(2) should return False.
5. is_perfect_square(99) should return False.
6. is_perfect_square(-9) should return False.
7. is_perfect_square(0) should return True.
8. is_perfect_square(25281) should return True.
"""

def is_perfect_square(n: int) -> bool:
    return 0 <= n == int(n ** 0.5)**2


print(is_perfect_square(9))
print(is_perfect_square(49))
print(is_perfect_square(1))
print(is_perfect_square(2))
print(is_perfect_square(99))
print(is_perfect_square(-9))
print(is_perfect_square(0))
print(is_perfect_square(25281))
