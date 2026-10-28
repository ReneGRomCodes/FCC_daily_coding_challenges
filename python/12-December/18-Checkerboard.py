"""
Checkerboard
Given an array with two numbers, the first being the number of rows and the second being the number of columns, return
a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

The characters should alternate like a checkerboard.
The top-left cell must always be "X".
For example, given [3, 3], return:

[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]

1. create_board([3, 3]) should return [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]].
2. create_board([6, 1]) should return [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]].
3. create_board([2, 10])
    should return [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]].
4. create_board([5, 4])
    should return [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]].
"""

def create_board(dimensions: list[int]) -> list[list[str]]:
    n_rows, n_columns = dimensions
    placeholder: str = "."
    value_switch: dict[str, str] = {
        "X": "O",
        "O": "X",
    }

    # Create complete matrix with placeholder values.
    matrix: list[list[str]] = [[placeholder for _ in range(n_columns)] for _ in range(n_rows)]

    for i, row in enumerate(matrix):
        for j, field in enumerate(row):
            if (i, j) == (0, 0):
                matrix[i][j] = value_switch["O"]  # Set first field in matrix to "X".
            elif i == 0:
                row[j] = value_switch[row[j-1]]
            elif i != 0:
                row[j] = value_switch[matrix[i-1][j]]

    return matrix


print(create_board([3, 3]))
print(create_board([6, 1]))
print(create_board([2, 10]))
print(create_board([5, 4]))
