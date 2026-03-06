/*
Trail Traversal
Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

"C": Your current location
"G": Your goal
"T": Traversable parts of the trail
"-": Untraversable parts of the map

Return a string with the moves needed to follow the trail from your location to your goal where:

"R" is a move right
"D" is a move down
"L" is a move left
"U" is a move up

There will always be a single continuous trail, without any branching, from your current location to your goal.
Each trail location will have a maximum of two traversable locations touching it.

For example, given:

[
  "-CT--",
  "--T--",
  "--TT-",
  "---T-",
  "---G-"
]
Return "RDDRDD".

1. navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]) should return "RDDRDD".
2. navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"]) should return "RRUUURR".
3. navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]) should return "DLDDRRRRD".
4. navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]) should return "RRRDDL".
5. navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]) should return "ULLLUUURRRRRRDDDR".
 */

function navigateTrail(map) {
    const rows = map.length;
    const cols = map[0].length;

    const dirs = [
        [0, 1, "R"],
        [1, 0, "D"],
        [0, -1, "L"],
        [-1, 0, "U"]
    ];

    let cur = null;

    // Find start.
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (map[r][c] === "C") {
                cur = [r, c];
            }
        }
    }

    let prev = null;
    let result = "";

    while (map[cur[0]][cur[1]] !== "G") {
        const [r, c] = cur;

        for (const [dr, dc, move] of dirs) {
            const nr = r + dr;
            const nc = c + dc;

            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            if (prev && nr === prev[0] && nc === prev[1]) continue;

            if (map[nr][nc] === "T" || map[nr][nc] === "G") {
                result += move;
                prev = cur;
                cur = [nr, nc];
                break;
            }
        }
    }

    return result;
}


console.log(navigateTrail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]));
console.log(navigateTrail(["-----", "--TTG", "--T--", "--T--", "CTT--"]));
console.log(navigateTrail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]));
console.log(navigateTrail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]));
console.log(navigateTrail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]));
