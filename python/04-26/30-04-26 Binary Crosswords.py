"""
Binary Crossword

Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or
vertically in either direction:

0 1 0 0 0 0 0 1
0 1 1 0 1 1 1 1
0 1 0 0 0 1 0 0
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0
0 1 0 1 0 1 0 0
0 1 1 0 1 0 0 0
1 0 1 0 1 1 1 0

For example, "A" has the binary representation 01000001, which appears in the first row from left to right.

1. isInCrossword("I") should return true.
2. isInCrossword("D") should return true.
3. isInCrossword("0") should return true.
4. isInCrossword("u") should return true.
5. isInCrossword("Y") should return false.
6. isInCrossword("p") should return false.
7. isInCrossword("1") should return false.
8. isInCrossword("Q") should return false.
"""

def get_rotated_grid(grid: list[str]) -> list[str]:
    return ["".join(row[i] for row in grid) for i in range(len(grid[0]))]


def check_grid_for_binary(binary: str, grid: list[str]) -> bool:
    return any(binary in row or binary in row[::-1] for row in grid)


def is_in_crossword(char: str) -> bool:
    bin_grid = [
        "01000001",
        "01101111",
        "01000100",
        "01100101",
        "01010010",
        "01010100",
        "01101000",
        "10101110"
    ]

    rotated = get_rotated_grid(bin_grid)
    char_bin = format(ord(char), "08b")

    return check_grid_for_binary(char_bin, bin_grid) or check_grid_for_binary(char_bin, rotated)


print(is_in_crossword("I"))
print(is_in_crossword("D"))
print(is_in_crossword("0"))
print(is_in_crossword("u"))
print(is_in_crossword("Y"))
print(is_in_crossword("p"))
print(is_in_crossword("1"))
print(is_in_crossword("Q"))
