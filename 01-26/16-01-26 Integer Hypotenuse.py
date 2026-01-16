"""
Integer Hypotenuse
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle,
determine whether the hypotenuse is an integer.

The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the
square root of that total (a² + b² = c²).

1. is_integer_hypotenuse(3, 4) should return True.
2. is_integer_hypotenuse(2, 3) should return False.
3. is_integer_hypotenuse(5, 12) should return True.
4. is_integer_hypotenuse(10, 10) should return False.
5. is_integer_hypotenuse(780, 1040) should return True.
6. is_integer_hypotenuse(250, 333) should return False.
"""

# Usually I go for a 'no imports' solution with these challenges, but I just couldn't be bothered to calculate the square
# root here manually... so here we go.
import math

def is_integer_hypotenuse(a: int, b: int) -> bool:
    if math.sqrt(a**2 + b**2) % 1 == 0:
        return True

    return False


print(is_integer_hypotenuse(3, 4))
print(is_integer_hypotenuse(2, 3))
print(is_integer_hypotenuse(5, 12))
print(is_integer_hypotenuse(10, 10))
print(is_integer_hypotenuse(780, 1040))
print(is_integer_hypotenuse(250, 333))
