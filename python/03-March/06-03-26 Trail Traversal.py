"""
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
"""

def navigate_trail(map: list[str]) -> str:
    grid: list[list[str]] = [list(row) for row in map]
    rows, cols = len(grid), len(grid[0])

    directions: dict[str, tuple[int, int]] = {
        "R": (0, 1),
        "L": (0, -1),
        "D": (1, 0),
        "U": (-1, 0)
    }

    # Find start.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "C":
                cur = (r, c)

    prev = None
    path = []

    while grid[cur[0]][cur[1]] != "G":
        r, c = cur

        for move, (dr, dc) in directions.items():
            nr, nc = r + dr, c + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            if (nr, nc) == prev:
                continue

            if grid[nr][nc] in ("T", "G"):
                path.append(move)
                prev = cur
                cur = (nr, nc)
                break

    return "".join(path)


print(navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]))
print(navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"]))
print(navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]))
print(navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]))
print(navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]))
