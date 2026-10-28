"""
Nonogram Validator
Given an array of clue numbers and an array of cells, determine whether the cells satisfy the nonogram clue.

- The clue is an array of numbers representing the lengths of consecutive filled cells, in order. For example, a clue of
  [3, 2] means there should be 3 consecutive filled cells followed by 2 consecutive filled cells, separated by at least one empty cell.
- The row is an array of 1s (filled) and 0s (empty).

1. is_valid_nonogram([3, 2], [1, 1, 1, 0, 1, 1]) should return True.
2. is_valid_nonogram([3, 2], [0, 1, 1, 1, 1, 1]) should return False.
3. is_valid_nonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]) should return False.
4. is_valid_nonogram([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]) should return True.
5. is_valid_nonogram([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]) should return True.
6. is_valid_nonogram([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) should return False.
"""

def is_valid_nonogram(clue: list[int], cells: list[int]) -> bool:
    target_cells: list[int] = []
    cleaned_cells: list[int] = []

    # Populate 'target_cells' based on 'clue'.
    for i, n in enumerate(clue):

        for _ in range(n):
            target_cells.append(1)

        if i != len(clue) - 1:
            target_cells.append(0)

    # Clean 'cells' to only have one 0 in between populated cells.
    for i, m in enumerate(cells):
        if m == 0 and i != 0 and cells[i - 1] != 0 and i != len(cells) - 1:
            cleaned_cells.append(m)
        elif m == 1:
            cleaned_cells.append(m)

    # Drop trailing 0 that the previous loop didn't catch.
    if cleaned_cells[-1] == 0:
        cleaned_cells.pop()

    return target_cells == cleaned_cells


print(is_valid_nonogram([3, 2], [1, 1, 1, 0, 1, 1]))
print(is_valid_nonogram([3, 2], [0, 1, 1, 1, 1, 1]))
print(is_valid_nonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]))
print(is_valid_nonogram([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]))
print(is_valid_nonogram([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]))
print(is_valid_nonogram([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
