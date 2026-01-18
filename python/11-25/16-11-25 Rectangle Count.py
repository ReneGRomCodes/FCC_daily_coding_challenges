"""
Rectangle Count
Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in
the given one.

Only count rectangles with integer width and height.
For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.

1. count_rectangles(1, 3) should return 6.
2. count_rectangles(3, 2) should return 18.
3. count_rectangles(1, 2) should return 3.
4. count_rectangles(5, 4) should return 150.
5. count_rectangles(11, 19) should return 12540.
"""

def count_rectangles(width: int, height :int) -> int:
    return int((width * (width + 1) * height * (height + 1)) / 4)


print(count_rectangles(1, 3))
print(count_rectangles(3, 2))
print(count_rectangles(1, 2))
print(count_rectangles(5, 4))
print(count_rectangles(11, 19))
