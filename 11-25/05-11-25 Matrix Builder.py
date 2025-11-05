"""
Matrix Builder
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros
(0) of the given size.

For example, given 2 and 3, return:

[
  [0, 0, 0],
  [0, 0, 0]
]

1. build_matrix(2, 3) should return [[0, 0, 0], [0, 0, 0]].
2. build_matrix(3, 2) should return [[0, 0], [0, 0], [0, 0]].
3. build_matrix(4, 3) should return [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]].
4. build_matrix(9, 1) should return [[0], [0], [0], [0], [0], [0], [0], [0], [0]].
"""

def build_matrix(rows: int, cols: int) -> list[list[int]]:
    filler: int = 0

    return [[filler] * cols] * rows


print(build_matrix(2, 3))
print(build_matrix(3, 2))
print(build_matrix(4, 3))
print(build_matrix(9, 1))
