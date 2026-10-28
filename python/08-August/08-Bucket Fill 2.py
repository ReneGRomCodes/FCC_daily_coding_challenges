"""
Bucket Fill 2
Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks"
needed to make the entire grid the target color.

- Each click changes the clicked cell's color and the entire region of connected cells of the same color with the target color.
- Cells are connected horizontally and vertically (not diagonally).

1. bucket_fill([["R", "R"], ["R", "R"]], "G") should return 1.
2. bucket_fill([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]], "B") should return 0.
3. bucket_fill([["G", "Y", "Y"], ["G", "Y", "G"], ["Y", "Y", "G"]], "R") should return 3.
4. bucket_fill([["G", "G", "P", "Y"], ["O", "P", "P", "P"], ["O", "O", "P", "G"], ["G", "O", "O", "G"]], "P") should return 5.
5. bucket_fill([["G", "G", "C", "C", "O"], ["B", "Y", "B", "Y", "O"], ["B", "J", "O", "J", "B"], ["G", "Y", "Y", "Y", "B"], ["G", "P", "P", "G", "G"]], "Y")
    should return 12.
"""

def bucket_fill(grid: list[list[str]], target_color: str) -> int:
    rows: int = len(grid)
    cols: int = len(grid[0])
    visited: set[tuple[int, int]] = set()
    directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1),]

    regions: int = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == target_color or (row, col) in visited:
                continue

            regions += 1
            colour = grid[row][col]
            stack = [(row, col)]
            visited.add((row, col))

            while stack:
                current_row, current_col = stack.pop()

                for dr, dc in directions:
                    new_row: int = current_row + dr
                    new_col: int = current_col + dc

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == colour
                        and (new_row, new_col) not in visited
                    ):
                        visited.add((new_row, new_col))
                        stack.append((new_row, new_col))

    return regions


print(bucket_fill([["R", "R"], ["R", "R"]], "G"))
print(bucket_fill([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]], "B"))
print(bucket_fill([["G", "Y", "Y"], ["G", "Y", "G"], ["Y", "Y", "G"]], "R"))
print(bucket_fill([["G", "G", "P", "Y"], ["O", "P", "P", "P"], ["O", "O", "P", "G"], ["G", "O", "O", "G"]], "P"))
print(bucket_fill([["G", "G", "C", "C", "O"], ["B", "Y", "B", "Y", "O"], ["B", "J", "O", "J", "B"], ["G", "Y", "Y", "Y", "B"], ["G", "P", "P", "G", "G"]], "Y"))
