"""
Connect 3
Given a matrix of strings representing pieces on a game grid, determine if any player has three in a row.

- Each cell contains "R", "Y", or "" (empty string).
- Three in a row means three consecutive non-empty cells of the same type horizontally, vertically, or diagonally.

Return:
- A flat array with the winner and the coordinates of their three winning cells in the format: ["R", [0,2], [1,3], [2,4]].
  Coordinates are returned top-to-bottom, then left-to-right.
- An empty array if there is no winner.

1. connectThree([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]) should return ["R", [3, 1], [3, 2], [3, 3]].
2. connectThree([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]) should return ["Y", [1, 1], [2, 1], [3, 1]].
3. connectThree([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]]) should return ["R", [0, 3], [1, 2], [2, 1]].
4. connectThree([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]) should return ["Y", [0, 1], [1, 2], [2, 3]].
5. connectThree([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]) should return [].
"""

def connect_three(matrix: list[list[str]]) -> list:
    matrix_height: int = len(matrix)
    matrix_width: int = len(matrix[0])
    search_directions: tuple[tuple[int, int], ...] = ((0, 1), (1, 0), (1, 1), (1, -1))

    for row in range(matrix_height):
        for col in range(matrix_width):
            player: str = matrix[row][col]

            if player == "":
                continue

            for row_step, col_step in search_directions:
                end_row: int = row + row_step * 2
                end_col: int = col + col_step * 2

                if not (0 <= end_row < matrix_height and 0 <= end_col < matrix_width):
                    continue

                if matrix[row + row_step][col + col_step] == player and matrix[end_row][end_col] == player:
                    return [player, [row, col], [row + row_step, col + col_step], [end_row, end_col]]

    return []


print(connect_three([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]))
print(connect_three([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]))
print(connect_three([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]]))
print(connect_three([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]))
print(connect_three([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]))
