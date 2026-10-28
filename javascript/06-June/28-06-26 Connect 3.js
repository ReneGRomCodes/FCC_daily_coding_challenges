/*
Connect 3
Given a matrix of strings representing pieces on a game grid, determine if any player has three in a row.

- Each cell contains "R", "Y", or "" (empty string).
- Three in a row means three consecutive non-empty cells of the same type horizontally, vertically, or diagonally.

Return:
- A flat array with the winner and the coordinates of their three winning cells in the format: ["R", [0,2], [1,3], [2,4]].
  Coordinates are returned top-to-bottom, then left-to-right.
- An empty array if there is no winner.

1. connectThree([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]) should return ["R", [3, 1], [3, 2], [3, 3]].
2. connectThree([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]) should return ["Y", [1, 1], [2, 1], [3, 1]].
3. connectThree([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]]) should return ["R", [0, 3], [1, 2], [2, 1]].
4. connectThree([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]) should return ["Y", [0, 1], [1, 2], [2, 3]].
5. connectThree([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]) should return [].
 */

function connectThree(matrix) {
    const matrixHeight = matrix.length;
    const matrixWidth = matrix[0].length;
    const searchDirections = [[0, 1], [1, 0], [1, 1], [1, -1]];

    for (let row = 0; row < matrixHeight; row++) {
        for (let col = 0; col < matrixWidth; col++) {
            const player = matrix[row][col];

            if (player === "") {
                continue;
            }

            for (const [rowStep, colStep] of searchDirections) {
                const endRow = row + rowStep * 2;
                const endCol = col + colStep * 2;

                if (!(endRow >= 0 && endRow < matrixHeight && endCol >= 0 && endCol < matrixWidth)) {
                    continue;
                }

                if (matrix[row + rowStep][col + colStep] === player && matrix[endRow][endCol] === player) {
                    return [player, [row, col], [row + rowStep, col + colStep], [endRow, endCol]];
                }
            }
        }
    }

    return [];
}


console.log(connectThree([["", "", "", ""], ["", "", "", ""], ["", "Y", "", ""], ["Y", "R", "R", "R"]]));
console.log(connectThree([["", "", "", ""], ["", "Y", "Y", ""], ["", "Y", "R", "R"], ["", "Y", "R", "R"]]));
console.log(connectThree([["", "", "Y", "R"], ["", "Y", "R", "Y"], ["", "R", "Y", "R"], ["", "R", "Y", "R"]]));
console.log(connectThree([["", "Y", "", ""], ["", "Y", "Y", ""], ["", "R", "R", "Y"], ["R", "R", "Y", "R"]]));
console.log(connectThree([["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"], ["Y", "R", "R", "Y"], ["R", "Y", "Y", "R"]]));
