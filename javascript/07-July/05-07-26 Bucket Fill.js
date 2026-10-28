/*
Bucket Fill
Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all
connected cells of the same value with the new value.

- Cells are connected if they are adjacent horizontally or vertically (not diagonally).

Return the updated grid.

1. bucket_fill([["R", "G"], ["R", "G"]], [0, 1], "B") should return [["R", "B"], ["R", "B"]].
2. bucket_fill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B") should return [["B", "G", "G"], ["B", "B", "B"], ["B", "B", "R"]].
3. bucket_fill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R") should return [["O", "O", "P"], ["R", "O", "O"], ["R", "R", "O"]].
4. bucket_fill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y")
    should return [["Y", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["R", "Y", "R", "Y"], ["Y", "Y", "Y", "Y"]].
5. bucket_fill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G")
    should return [["G", "G", "G", "B"], ["R", "G", "G", "G"], ["B", "G", "G", "R"], ["B", "G", "G", "B"]].
 */

function bucketFill(grid, [row, col], newValue) {
    const rows = grid.length;
    const cols = grid[0].length;
    const [startRow, startCol] = [row, col];
    const target = grid[startRow][startCol];

    if (target === newValue) {
        return grid;
    }

    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

    const stack = [[startRow, startCol]];

    while (stack.length > 0) {
        const [row, col] = stack.pop();

        if (grid[row][col] !== target) {
            continue;
        }

        grid[row][col] = newValue;

        for (const [dr, dc] of directions) {
            const newRow = row + dr;
            const newCol = col + dc;

            if (
                newRow >= 0 &&
                newRow < rows &&
                newCol >= 0 &&
                newCol < cols &&
                grid[newRow][newCol] === target
            ) {
                stack.push([newRow, newCol]);
            }
        }
    }

    return grid;
}


console.log(bucketFill([["R", "G"], ["R", "G"]], [0, 1], "B"));
console.log(bucketFill([["Y", "G", "G"], ["Y", "Y", "Y"], ["B", "Y", "R"]], [1, 2], "B"));
console.log(bucketFill([["O", "O", "P"], ["P", "O", "O"], ["P", "P", "O"]], [2, 0], "R"));
console.log(bucketFill([["T", "T", "R", "T"], ["R", "T", "R", "T"], ["R", "T", "R", "T"], ["T", "T", "T", "T"]], [0, 3], "Y"));
console.log(bucketFill([["G", "B", "G", "B"], ["R", "B", "B", "G"], ["B", "G", "B", "R"], ["B", "G", "G", "B"]], [2, 2], "G"));
