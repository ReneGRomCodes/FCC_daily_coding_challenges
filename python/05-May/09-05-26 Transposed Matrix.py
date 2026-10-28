"""
Transposed Matrix

Given a matrix (an array of arrays), return the transposed version of it.
To transpose the matrix, swap the rows and columns. E.g: a value at index [0, 1] should move to index [1, 0].

For example, given:
[
  [1, 2, 3],
  [4, 5, 6]
]

Return:
[
  [1, 4],
  [2, 5],
  [3, 6]
]

1. transpose([[1, 2, 3], [4, 5, 6]]) should return [[1, 4], [2, 5], [3, 6]].
2. transpose([[1, 2], [3, 4], [5, 6]]) should return [[1, 3, 5], [2, 4, 6]].
3. transpose([[1, 2], [3, 4], [5, 6], [7, 8]]) should return [[1, 3, 5, 7], [2, 4, 6, 8]].
4. transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]])
    should return [["a", "d", "g", "j"], ["b", "e", "h", "k"], ["c", "f", "i", "l"]].
5. transpose([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]])
    should return [[True, False, True, False, True], [False, True, True, False, False], [True, False, False, True, False], [False, True, False, True, True]].
"""

def transpose(matrix: list[list]) -> list[list]:
    n_cols: int = len(matrix[0])
    n_rows: int = len(matrix)
    transposed_matrix: list[list] = []

    for i in range(n_cols):
        new_row = []
        for j in range(n_rows):
            new_row.append(matrix[j][i])

        transposed_matrix.append(new_row)

    return transposed_matrix


print(transpose([[1, 2, 3],
                 [4, 5, 6]]))
print(transpose([[1, 2],
                 [3, 4],
                 [5, 6]]))
print(transpose([[1, 2],
                 [3, 4],
                 [5, 6],
                 [7, 8]]))
print(transpose([["a", "b", "c"],
                 ["d", "e", "f"],
                 ["g", "h", "i"],
                 ["j", "k", "l"]]))
print(transpose([[True, False, True, False],
                 [False, True, False, True],
                 [True, True, False, False],
                 [False, False, True, True],
                 [True, False, False, True]]))
