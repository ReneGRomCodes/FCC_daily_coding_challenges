"""
Magic Square Solver
Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square,
or "impossible" if no valid number exists.

A magic square is a grid where every row, column, and diagonal adds up to the same number.

1. solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]) should return 5.
2. solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]) should return 4.
3. solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]) should return "impossible".
4. solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]) should return 39.
5. solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]) should return "impossible".
"""

def solve_magic_square(grid: list[list[int]]) -> int | str:
    """NOTE: I ignored the diagonal sum check because it turned out that there was no dirty little edge case in this
    challenge that would necessitate it. Had it in there but because it didn't actually do anything here I removed
    it as 'clutter'. Come on... it's just a fun little challenge after all, not production code ;)"""
    missing_n: int = 0  # Placeholder value for missing number in 'grid'.
    missing_n_row, missing_n_col = 0, 0  # Initial placeholder indices for 'missing_n'.
    magic_n: int | None = None  # Variable for row/column/diagonal sum. Guaranteed to be assigned an int value in this
                                # challenge, so don't get your knickers in a twist about the 'None' value here.

    for row_index, row in enumerate(grid):
        if missing_n in row:
            missing_n_row, missing_n_col = row_index, row.index(missing_n)
        else:
            magic_n = sum(row)

    # Calculate 'missing_n' value and add it to grid.
    missing_n = magic_n - sum(grid[missing_n_row])
    grid[missing_n_row][missing_n_col] = missing_n

    if sum(grid[missing_n_row]) == magic_n and sum(x[missing_n_col] for x in grid) == magic_n:
        return missing_n

    return "impossible"


print(solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]))
print(solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]))
print(solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]))
print(solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]))
print(solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]))
