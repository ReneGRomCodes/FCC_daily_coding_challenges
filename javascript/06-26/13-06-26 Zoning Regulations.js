/*
Zoning Regulations
Given a 2D grid (array of arrays) representing a city's building layout, return the coordinates of all buildings that are
violating zoning rules.

Each cell in the grid contains one of the labels from the table below. A building is in violation if any of its (up to)
4 neighbors, horizontal or vertical, are a type it cannot be adjacent to.

Label	Type	        Cannot be adjacent to
"i"	    industrial	    "R", "I"
"A"	    Agricultural	"C"
"R"	    Residential	    "i", "C"
"I"	    Institutional	"i"
"C"	    Commercial	    "R", "A"
""      undeveloped	    no restrictions

Return the coordinates of all violating cells as an array of [row, col] pairs, in any order. If no violations exist,
return an empty array.

1. get_zone_violations([["R", "C"], ["", "C"]]) should return [[0, 0], [0, 1]].
2. get_zone_violations([["", "i"], ["", "R"], ["R", "I"]]) should return [[0, 1], [1, 1]].
3. get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]) should return [].
4. get_zone_violations([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]])
    should return [[0, 1], [0, 2], [0, 3]].
5. get_zone_violations([["R", "A", "A", "", "i", "i"], ["R", "I", "", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]])
    should return [[2, 3], [2, 4], [3, 1], [3, 2]].
 */

function getZoneViolations(grid) {
    const restrictions = {
        "i": ["R", "I"],
        "A": ["C"],
        "R": ["i", "C"],
        "I": ["i"],
        "C": ["R", "A"]
    };
    const violatingCells = [];
    const rows = grid.length;
    const cols = grid[0].length;
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            let currentCell = grid[i][j]

            if (!restrictions[currentCell]) {
                continue;
            }

            let cellRestrictions = restrictions[currentCell];
            let isViolating = false;

            for (const [deltaI, deltaJ] of directions) {
                const nextI = i + deltaI;
                const nextJ = j + deltaJ;

                if (nextI >= 0 && nextI < rows && nextJ >= 0 && nextJ < cols) {
                    let neighborCell = grid[nextI][nextJ];

                    if (cellRestrictions.includes(neighborCell)) {
                        isViolating = true;
                        break;
                    }
                }
            }
            if (isViolating) {
                violatingCells.push([i, j]);
            }
        }
    }

    return violatingCells;
}


console.log(getZoneViolations([["R", "C"], ["", "C"]]));
console.log(getZoneViolations([["", "i"], ["", "R"], ["R", "I"]]));
console.log(getZoneViolations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]));
console.log(getZoneViolations([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]]));
console.log(getZoneViolations([["R", "A", "A", "", "i", "i"], ["R", "I", "", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]]));