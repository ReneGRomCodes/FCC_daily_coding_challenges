/*
Transposed Matrix

Given a matrix (an array of arrays), return the transposed version of it.
To transpose the matrix, swap the rows and columns. E.g: a value at index [0, 1] should move to index [1, 0].

For example, given:
[
  [1, 2, 3],
  [4, 5, 6]
]

Return:
[
  [1, 4],
  [2, 5],
  [3, 6]
]

1. transpose([[1, 2, 3], [4, 5, 6]]) should return [[1, 4], [2, 5], [3, 6]].
2. transpose([[1, 2], [3, 4], [5, 6]]) should return [[1, 3, 5], [2, 4, 6]].
3. transpose([[1, 2], [3, 4], [5, 6], [7, 8]]) should return [[1, 3, 5, 7], [2, 4, 6, 8]].
4. transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]])
    should return [["a", "d", "g", "j"], ["b", "e", "h", "k"], ["c", "f", "i", "l"]].
5. transpose([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]])
    should return [[True, False, True, False, True], [False, True, True, False, False], [True, False, False, True, False], [False, True, False, True, True]].
 */

function transpose(matrix) {
    const nCols = matrix[0].length;
    const nRows = matrix.length;
    const transposedMatrix = [];

    for (let i = 0; i < nCols; i++) {
        const newRow = [];

        for (let j = 0; j < nRows; j++) {
            newRow.push(matrix[j][i]);
        }

        transposedMatrix.push(newRow);
    }

    return transposedMatrix;
}


console.log(transpose([
    [1, 2, 3],
    [4, 5, 6]
]));
console.log(transpose([
    [1, 2],
    [3, 4],
    [5, 6]
]));
console.log(transpose([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]));
console.log(transpose([
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"]
]));
console.log(transpose([
    [true, false, true, false],
    [false, true, false, true],
    [true, true, false, false],
    [false, false, true, true],
    [true, false, false, true]
]));
