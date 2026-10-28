"""
Bucket Fill
Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all
connected cells of the same value with the new value.

- Cells are connected if they are adjacent horizontally or vertically (not diagonally).

Return the updated grid.

1. bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B") should return [["R", "B"], ["R", "B"]].
2. bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B") should return [["B", "G", "G"], ["B", "B", "B"], ["B", "B", "R"]].
3. bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R") should return [["O", "O", "P"], ["R", "O", "O"], ["R", "R", "O"]].
4. bucket_fill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y")
    should return [["Y", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["Y", "Y", "Y", "Y"]].
5. bucket_fill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G")
    should return [["G", "G", "G", "B"], ["R", "G", "G", "G"], ["B", "G", "G", "R"], ["B", "G", "G", "B"]].
"""

def bucket_fill(grid: list[list[str]], pos: list[int], new_value: str) -> list[list[str]]:
    rows: int = len(grid)
    cols: int = len(grid[0])
    start_row, start_col = pos
    target: str = grid[start_row][start_col]
    directions: tuple[tuple[int, int], ...] = ((-1, 0), (1, 0), (0, -1), (0, 1))
    stack: list[tuple[int, int]] = [(start_row, start_col)]

    while stack:
        row, col = stack.pop()

        # Skip cells that aren't part of the region.
        if grid[row][col] != target:
            continue

        # Fill the current cell.
        grid[row][col] = new_value

        # Visit all valid neighbours.
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == target:
                stack.append((new_row, new_col))

    return grid


print(bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B"))
print(bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"))
print(bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R"))
print(bucket_fill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y"))
print(bucket_fill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G"))
