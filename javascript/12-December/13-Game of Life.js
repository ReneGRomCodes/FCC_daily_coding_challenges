/*
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
 */

// Check surrounding cells for life and return number of live cells.
function countSurroundingLife(grid, i, j, isBorderLt, isBorderRt, isBorderUp, isBorderLo) {
    const liveCells = [
        !isBorderLt && grid[i][j - 1],  // left
        !isBorderRt && grid[i][j + 1],  // right
        !isBorderUp && grid[i - 1][j],  // top
        !isBorderLo && grid[i + 1][j],  // below
        (!isBorderUp && !isBorderLt) && grid[i - 1][j - 1],  // top-left
        (!isBorderUp && !isBorderRt) && grid[i - 1][j + 1],  // top-right
        (!isBorderLo && !isBorderLt) && grid[i + 1][j - 1],  // bottom-left
        (!isBorderLo && !isBorderRt) && grid[i + 1][j + 1]  // bottom-right
    ];

    return liveCells.filter(cell => cell === 1).length;
}

function gameOfLife(grid) {
    const newGrid = [];

    for (let i = 0; i < grid.length; i++) {
        const array = grid[i];
        const [isBorderUp, isBorderLo] = [i === 0, i === grid.length - 1];
        const newArray = [];

        for (let j = 0; j < array.length; j++) {
            const cell = array[j];
            const isCellAlive = cell === 1;
            const [isBorderLt, isBorderRt] = [j === 0, j === grid[0].length - 1];
            const nLiveCells = countSurroundingLife(grid, i, j, isBorderLt, isBorderRt, isBorderUp, isBorderLo)

            if (nLiveCells < 2 || (nLiveCells > 3 && isCellAlive)) { newArray.push(0) }
            else if (([2, 3].includes(nLiveCells) && isCellAlive) || (nLiveCells === 3 && !isCellAlive)) { newArray.push(1) }
            else { newArray.push(cell) }
        }

        newGrid.push(newArray);
    }

    return newGrid;
}


console.log(gameOfLife([[0, 1, 0], [0, 1, 1], [1, 1, 0]]));
console.log(gameOfLife([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]));
console.log(gameOfLife([[1, 0, 0], [0, 1, 0], [0, 0, 1]]));
console.log(gameOfLife([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]));
