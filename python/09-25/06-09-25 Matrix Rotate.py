"""
Matrix Rotate
Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. For instance, given
[[1, 2], [3, 4]], which looks like this:
1	2
3	4

You should return [[3, 1], [4, 2]], which looks like this:
3	1
4	2

1. rotate([[1]]) should return [[1]].
2. rotate([[1, 2], [3, 4]]) should return [[3, 1], [4, 2]].
3. rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return [[7, 4, 1], [8, 5, 2], [9, 6, 3]].
4. rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]) should return [[0, 1, 0], [0, 0, 1], [0, 1, 0]].
"""

def rotate(matrix: list[list[int]]) -> list[list[int]]:
    n: int = len(matrix)
    m: int = len(matrix[0])

    # Transpose the matrix
    transposed_matrix: list[list[int]] = [[matrix[j][i] for j in range(n)] for i in range(m)]

    # Reverse each row
    rotated_matrix = [[row[i] for i in range(m - 1, -1, -1)] for row in transposed_matrix]

    return rotated_matrix


print(rotate([[1]]))
print(rotate([[1, 2], [3, 4]]))
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]))
