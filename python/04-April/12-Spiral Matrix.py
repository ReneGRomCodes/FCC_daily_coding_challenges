"""
Spiral Matrix
Given a 2D matrix, return a flat array with all of its values in clockwise order.

The returned array should have the top-left value first, move right along the top row, then down the right column, then
left along the bottom row, then up the left column. Repeat inward for any remaining layers.

For example, given:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

Return [1, 2, 3, 6, 9, 8, 7, 4, 5].

1. spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    should return [1, 2, 3, 6, 9, 8, 7, 4, 5].
2. spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]])
    should return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"].
3. spiral_matrix([[True, False, False], [False, True, True], [False, True, False], [True, True, False]])
    should return [True, False, False, True, False, False, True, True, False, False, True, True].
4. spiral_matrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]])
    should return [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1].
"""

def spiral_matrix(matrix: list[list]) -> list:
    top: int = 0
    bottom: int = len(matrix) - 1
    left: int = 0
    right: int = len(matrix[0]) - 1
    result: list = []

    while top <= bottom and left <= right:

        # 1. Go right (top row).
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # 2. Go down (right column).
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # 3. Go left (bottom row).
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # 4. Go up (left column).
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]]))
print(spiral_matrix([[True, False, False], [False, True, True], [False, True, False], [True, True, False]]))
print(spiral_matrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]]))
