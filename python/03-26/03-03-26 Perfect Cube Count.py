"""
Perfect Cube Count
Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube
because 3 * 3 * 3 = 27.

1. count_perfect_cubes(3, 30) should return 2.
2. count_perfect_cubes(1, 30) should return 3.
3. count_perfect_cubes(30, 0) should return 4.
4. count_perfect_cubes(-64, 64) should return 9.
5. count_perfect_cubes(9214, -8127) should return 41.
"""
import math

def count_perfect_cubes(a: int, b: int) -> int:
    """Not the most optimal solution, but I wanted to fiddle around with the floating point problem in the for-loop a
    bit."""
    cube_range: list[int] = [min([a, b]), max([a, b]) + 1]
    counter: int = 0

    for i in range(cube_range[0], cube_range[1]):
        if round(math.cbrt(i)) ** 3 == i:
            counter +=1

    return counter


def count_perfect_cubes_optimized(a: int, b: int) -> int:
    """Optimized solution."""
    lower: int = min(a, b)
    upper: int = max(a, b)

    start: int = math.ceil(lower ** (1/3))
    end: int = math.floor(upper ** (1/3))

    return max(0, end - start + 1)


print(count_perfect_cubes(3, 30))
print(count_perfect_cubes(1, 30))
print(count_perfect_cubes(30, 0))
print(count_perfect_cubes(-64, 64))
print(count_perfect_cubes(9214, -8127))
