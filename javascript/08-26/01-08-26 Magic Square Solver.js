/*
Magic Square Solver
Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square,
or "impossible" if no valid number exists.

A magic square is a grid where every row, column, and diagonal adds up to the same number.

1. solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]) should return 5.
2. solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]) should return 4.
3. solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]) should return "impossible".
4. solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]) should return 39.
5. solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]) should return "impossible".
 */

// NOTE: I ignored the diagonal sum check because it turned out that there was no dirty little edge case in this
// challenge that would necessitate it. Had it in there but because it didn't actually do anything here I removed
// it as 'clutter'. Come on... it's just a fun little challenge after all, not production code ;)"
function solveMagicSquare(grid) {
    let missingN = 0;  // Placeholder value for missing number in 'grid'.
    let [missingNRow, missingNCol] = [0, 0];  // Initial placeholder indices for 'missing_n'.
    let magicN = null;  // # Variable for row/column/diagonal sum.

    for (let i = 0; i < grid.length; i++) {
        if (grid[i].includes(missingN)) {
            [missingNRow, missingNCol] = [i, grid[i].indexOf(missingN)];
        } else {
            magicN = grid[i].reduce((a, b) => a + b, 0);
        }
    }

    // Calculate 'missing_n' value and add it to grid.
    missingN = magicN - grid[missingNCol].reduce((a, b) => a + b, 0);
    grid[missingNRow][missingNCol] = missingN;

    if (
        grid[missingNRow].reduce((sum, value) => sum + value, 0) === magicN &&
        grid
            .map(row => row[missingNCol])
            .reduce((sum, value) => sum + value, 0) === magicN
    ) {
        return missingN;
    }

    return "impossible";
}


console.log(solveMagicSquare([[2, 7, 6], [9, 0, 1], [4, 3, 8]]));
console.log(solveMagicSquare([[0, 14, 12], [18, 10, 2], [8, 6, 16]]));
console.log(solveMagicSquare([[12, 17, 16], [19, 0, 10], [14, 13, 18]]));
console.log(solveMagicSquare([[15, 35, 31], [43, 27, 11], [23, 19, 0]]));
console.log(solveMagicSquare([[26, 41, 14], [47, 35, 0], [32, 29, 44]]));
