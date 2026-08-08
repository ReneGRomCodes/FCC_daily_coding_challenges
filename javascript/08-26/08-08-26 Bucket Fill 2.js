/*
Bucket Fill 2
Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks"
needed to make the entire grid the target color.

- Each click changes the clicked cell's color and the entire region of connected cells of the same color with the target color.
- Cells are connected horizontally and vertically (not diagonally).

1. bucket_fill([["R", "R"], ["R", "R"]], "G") should return 1.
2. bucket_fill([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]], "B") should return 0.
3. bucket_fill([["G", "Y", "Y"], ["G", "Y", "G"], ["Y", "Y", "G"]], "R") should return 3.
4. bucket_fill([["G", "G", "P", "Y"], ["O", "P", "P", "P"], ["O", "O", "P", "G"], ["G", "O", "O", "G"]], "P") should return 5.
5. bucket_fill([["G", "G", "C", "C", "O"], ["B", "Y", "B", "Y", "O"], ["B", "J", "O", "J", "B"], ["G", "Y", "Y", "Y", "B"], ["G", "P", "P", "G", "G"]], "Y")
    should return 12.
 */

function bucketFill(grid, targetColor) {
    const rows = grid.length;
    const cols = grid[0].length;
    const visited = new Set();

    const directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ];

    let regions = 0;

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const position = `${row},${col}`;

            if (grid[row][col] === targetColor || visited.has(position)) {
                continue;
            }

            regions++;

            const color = grid[row][col];
            const stack = [[row, col]];
            visited.add(position);

            while (stack.length > 0) {
                const [currentRow, currentCol] = stack.pop();

                for (const [dr, dc] of directions) {
                    const newRow = currentRow + dr;
                    const newCol = currentCol + dc;
                    const newPosition = `${newRow},${newCol}`;

                    if (
                        newRow >= 0 &&
                        newRow < rows &&
                        newCol >= 0 &&
                        newCol < cols &&
                        grid[newRow][newCol] === color &&
                        !visited.has(newPosition)
                    ) {
                        visited.add(newPosition);
                        stack.push([newRow, newCol]);
                    }
                }
            }
        }
    }

    return regions;
}


console.log(bucketFill([["R", "R"], ["R", "R"]], "G"));
console.log(bucketFill([["B", "B", "B"], ["B", "B", "B"], ["B", "B", "B"]], "B"));
console.log(bucketFill([["G", "Y", "Y"], ["G", "Y", "G"], ["Y", "Y", "G"]], "R"));
console.log(bucketFill([["G", "G", "P", "Y"], ["O", "P", "P", "P"], ["O", "O", "P", "G"], ["G", "O", "O", "G"]], "P"));
console.log(bucketFill([["G", "G", "C", "C", "O"], ["B", "Y", "B", "Y", "O"], ["B", "J", "O", "J", "B"],
    ["G", "Y", "Y", "Y", "B"], ["G", "P", "P", "G", "G"]], "Y"));
