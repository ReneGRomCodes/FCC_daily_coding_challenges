"""
Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the
matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]

return:
[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]

Each cell updates according to the number of live neighbors. For instance, [0][0] stays dead (2 live neighbors), [0][1]
stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on.

1. game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]) should return [[0, 1, 1], [0, 0, 1], [1, 1, 1]].
2. game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]])
    should return [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]].
3. game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) should return [[0, 0, 0], [0, 1, 0], [0, 0, 0]].
4. game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]])
    should return [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]].
"""

def count_surrounding_life(grid, i, j, is_border_lt, is_border_rt, is_border_up, is_border_lo) -> int:
    """Check surrounding cells for life and return number of live cells."""
    live_cells: list[bool] = [
        not is_border_lt and grid[i][j-1],  # left
        not is_border_rt and grid[i][j+1],  # right
        not is_border_up and grid[i-1][j],  # top
        not is_border_lo and grid[i+1][j],  # below
        (not is_border_up and not is_border_lt) and grid[i-1][j-1],  # top-left
        (not is_border_up and not is_border_rt) and grid[i-1][j+1],  # top-right
        (not is_border_lo and not is_border_lt) and grid[i+1][j-1],  # bottom-left
        (not is_border_lo and not is_border_rt) and grid[i+1][j+1]  # bottom-right
    ]

    return live_cells.count(True)


def game_of_life(grid: list[list[int]]) -> list[list[int]]:
    new_grid: list[list[int]] = []

    for i, array in enumerate(grid):
        is_border_up, is_border_lo = (i == 0), (i == len(grid)-1)
        new_array: list[int] = []

        for j, cell in enumerate(array):
            is_cell_alive: bool = cell == 1
            is_border_lt, is_border_rt = (j == 0), (j == len(grid[0])-1)
            n_live_cells: int = count_surrounding_life(grid, i, j, is_border_lt, is_border_rt, is_border_up, is_border_lo)

            if (n_live_cells < 2) or (n_live_cells > 3 and is_cell_alive):
                new_array.append(0)
            elif (n_live_cells in {2, 3} and is_cell_alive) or (n_live_cells == 3 and not is_cell_alive):
                new_array.append(1)
            else:
                new_array.append(cell)

        new_grid.append(new_array)

    return new_grid


print(game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
print(game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]))
print(game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]))
