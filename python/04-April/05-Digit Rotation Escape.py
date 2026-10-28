"""
Digit Rotation Escape
Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.

A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.

- Check rotation 0 (the given number) first.
- Given numbers won't contain any zeros.
- Return the first rotation number if one is found, or "none" if not.

1. get_rotation(123) should return 0.
2. get_rotation(13579) should return 3.
3. get_rotation(24681) should return "none".
4. get_rotation(84138789345) should return 6.
"""

def get_rotation(n: int) -> int | str:
    n_str: str = str(n)
    length: int = len(n_str)

    for i in range(0, length):
        if int(n_str) % length == 0:
            return i
        else:
            n_str = n_str[1:] + n_str[0]

    return "none"


print(get_rotation(123))
print(get_rotation(13579))
print(get_rotation(24681))
print(get_rotation(84138789345))
