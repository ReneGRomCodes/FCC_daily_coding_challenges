/*
The Last Challenge: Bucket Fill 3
Today marks a year of daily coding challenges. This is the last new one for now. Good luck!

Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks"
needed to make the entire grid that color.

- Each click changes the clicked cell's color and the entire region of connected cells of the same color (4-directional).
- Clicks can use any color as an intermediate step, not just the target color.

1. bucketFill([["B", "B"], ["B", "B"]], "R") should return 1.
2. bucketFill([["G", "G", "G"], ["G", "G", "G"], ["G", "G", "G"]], "G") should return 0.
3. bucketFill([["P", "P", "Y"], ["Y", "P", "Y"], ["Y", "P", "P"]], "O") should return 2.
4. bucketFill([["G", "Y", "C", "C"], ["Y", "Y", "Y", "B"], ["C", "Y", "B", "B"], ["C", "B", "B", "C"]], "R") should return 4.
5. bucketFill([["G", "G", "O", "O"], ["G", "Y", "B", "Y"], ["B", "Y", "B", "Y"], ["B", "Y", "B", "Y"], ["G", "G", "G", "G"]], "P")
    should return 5.
6. bucketFill([["R", "G", "R", "G"], ["R", "G", "R", "G"], ["B", "B", "B", "B"], ["B", "B", "B", "B"], ["R", "G", "R", "G"]], "Y")
    should return 3.
 */

// Fuck it! No clue what they meant by intermediate colour, so I vibe coded this one. Yes, I admit it, because this
// was just ridiculous... and I can blame ChatGPT for this shitshow of a code ;)
function bucketFill(grid, targetColor) {
    const rows = grid.length;
    const cols = grid[0].length;
    const colors = [...new Set(grid.flat().concat(targetColor))];

    const serialize = grid => JSON.stringify(grid);

    const directions = [
        [-1, 0], [1, 0],
        [0, -1], [0, 1]
    ];

    const getRegions = grid => {
        const visited = new Set();
        const regions = [];

        grid.forEach((row, r) => row.forEach((color, c) => {
            const key = `${r},${c}`;

            if (visited.has(key)) return;

            const region = [];
            const stack = [[r, c]];
            visited.add(key);

            while (stack.length) {
                const [cr, cc] = stack.pop();
                region.push([cr, cc]);

                directions.forEach(([dr, dc]) => {
                    const nr = cr + dr;
                    const nc = cc + dc;
                    const next = `${nr},${nc}`;

                    if (
                        nr >= 0 && nr < rows &&
                        nc >= 0 && nc < cols &&
                        !visited.has(next) &&
                        grid[nr][nc] === color
                    ) {
                        visited.add(next);
                        stack.push([nr, nc]);
                    }
                });
            }

            regions.push(region);
        }));

        return regions;
    };

    const queue = [[grid, 0]];
    const seen = new Set([serialize(grid)]);

    for (let i = 0; i < queue.length; i++) {
        const [current, clicks] = queue[i];

        if (current.every(row => row.every(color => color === targetColor))) {
            return clicks;
        }

        getRegions(current).forEach(region => {
            colors.forEach(color => {
                const oldColor = current[region[0][0]][region[0][1]];

                if (color === oldColor) return;

                const next = current.map(row => [...row]);

                region.forEach(([r, c]) => {
                    next[r][c] = color;
                });

                const key = serialize(next);

                if (!seen.has(key)) {
                    seen.add(key);
                    queue.push([next, clicks + 1]);
                }
            });
        });
    }
}


console.log(bucketFill([["B", "B"], ["B", "B"]], "R"));
console.log(bucketFill([["G", "G", "G"], ["G", "G", "G"], ["G", "G", "G"]], "G"));
console.log(bucketFill([["P", "P", "Y"], ["Y", "P", "Y"], ["Y", "P", "P"]], "O"));
console.log(bucketFill([["G", "Y", "C", "C"], ["Y", "Y", "Y", "B"], ["C", "Y", "B", "B"], ["C", "B", "B", "C"]], "R"));
console.log(bucketFill([["G", "G", "O", "O"], ["G", "Y", "B", "Y"], ["B", "Y", "B", "Y"], ["B", "Y", "B", "Y"], ["G", "G", "G", "G"]], "P"));
console.log(bucketFill([["R", "G", "R", "G"], ["R", "G", "R", "G"], ["B", "B", "B", "B"], ["B", "B", "B", "B"], ["R", "G", "R", "G"]], "Y"));
