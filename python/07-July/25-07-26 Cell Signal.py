"""
Cell Signal
Given a grid containing three cell tower readings, determine the location of the phone.

- Each cell in the grid is either 0 (no tower) or a positive integer representing the number of cells to the phone, measured
  in a straight line: horizontal, vertical, or diagonal.
- Return the [row, col] of the cell that is the correct number of cells from all three towers.
- There is always exactly one solution.

1. find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]) should return [1, 2].
2. find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]) should return [2, 1].
3. find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]) should return [2, 2].
4. find_signal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) should return [3, 4].
5. find_signal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2]])
    should return [3, 3].
"""

def find_signal(grid: list[list[int]]) -> list[int]:
    towers: list[tuple[int, int, int]] = [(r, c, val) for r, row in enumerate(grid) for c, val in enumerate(row) if val > 0]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if all(max(abs(r - tr), abs(c - tc)) == d for tr, tc, d in towers):
                return [r, c]


print(find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]))
print(find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]))
print(find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]))
print(find_signal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(find_signal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2]]))
