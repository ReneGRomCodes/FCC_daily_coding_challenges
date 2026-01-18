"""
Word Search
Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word
in the matrix.

The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.
The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top
For example, given the matrix:

[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:
[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).

1. find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat") should return [[0, 1], [2, 1]].
2. find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog") should return [[0, 0], [0, 2]].
3. find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish")
    should return [[3, 3], [0, 3]].
4. find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox")
    should return [[1, 3], [1, 1]].
"""

def find_word(matrix: list[list[str]], word: str) -> list[list[int]] | None:
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    l: int = len(word)

    directions = [
        (1, 0),   # down
        (-1, 0),  # up
        (0, 1),   # right
        (0, -1)   # left
    ]

    for y in range(rows):
        for x in range(cols):
            if matrix[y][x] != word[0]:
                continue

            for dx, dy in directions:
                match = True
                for i in range(l):
                    cx = x + dx * i
                    cy = y + dy * i
                    if cx < 0 or cy < 0 or cx >= cols or cy >= rows or matrix[cy][cx] != word[i]:
                        match = False
                        break

                if match:
                    end_x: int = x + dx * (l - 1)
                    end_y: int = y + dy * (l - 1)

                    return [[y, x], [end_y, end_x]]


print(find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat"))
print(find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog"))
print(find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish"))
print(find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox"))
