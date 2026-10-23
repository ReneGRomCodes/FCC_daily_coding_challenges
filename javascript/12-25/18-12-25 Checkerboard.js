/*
Checkerboard
Given an array with two numbers, the first being the number of rows and the second being the number of columns, return
a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

The characters should alternate like a checkerboard.
The top-left cell must always be "X".
For example, given [3, 3], return:

[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]

1. create_board([3, 3]) should return [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]].
2. create_board([6, 1]) should return [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]].
3. create_board([2, 10])
    should return [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]].
4. create_board([5, 4])
    should return [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]].
 */

function createBoard(dimensions) {
    const [nRows, nColumns] = dimensions;
    const placeholder = ".";
    const valueSwitch = {"X": "O", "O": "X"};

    // Create complete matrix with placeholder values.
    const matrix = Array.from(
        { length: nRows },
        () => Array(nColumns).fill(placeholder)
    );

    for (let i = 0; i < matrix.length; i++) {
        const row = matrix[i];

        for (let j = 0; j < row.length; j++) {
            const field = row[j];

            if (i === 0 && j === 0) { matrix[i][j] = valueSwitch["O"] }  // Set first field in matrix to "X".
            else if (i === 0) { row[j] = valueSwitch[row[j-1]] }
            else if (i !== 0) { row[j] = valueSwitch[matrix[i-1][j]] }
        }
    }

    return matrix;
}


console.log(createBoard([3, 3]));
console.log(createBoard([6, 1]));
console.log(createBoard([2, 10]));
console.log(createBoard([5, 4]));
