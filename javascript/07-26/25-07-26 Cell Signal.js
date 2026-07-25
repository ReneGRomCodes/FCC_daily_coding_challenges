/*
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
 */

function findSignal(grid) {
    const towers = [];

    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            if (grid[r][c] > 0) towers.push([r, c, grid[r][c]]);
        }
    }

    for (let r = 0; r < grid.length; r++) {
        for (let c = 0; c < grid[0].length; c++) {
            let match = true;
            for (const [tr, tc, d] of towers) {
                if (Math.max(Math.abs(r - tr), Math.abs(c - tc)) !== d) {
                    match = false;
                    break;
                }
            }
            if (match) return [r, c];
        }
    }
}


console.log(findSignal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]));
console.log(findSignal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]));
console.log(findSignal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]));
console.log(findSignal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0], [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]));
console.log(findSignal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2]]));
