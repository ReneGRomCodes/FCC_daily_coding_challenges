"""
2026 Winter Games Day 16: Curling
Given a 5x5 matrix representing the "house" at the end of a curling round, determine which team scores and how many
points they score.

The layout:
The center cell (index [2, 2]) is the "button".
The 8 cells directly surrounding the button represent ring 1.
And the 16 cells on the outer edge of the house represent ring 2.
In the given matrix:

"." represents an empty space.
"R" represents a space with a red stone.
"Y" represents a space with a yellow stone.
Scoring rules:

Only one team can score per round.
The team with the stone closest to the button scores.
The scoring team earns 1 point for each of their stones that is closer to the button than the opponent's closest stone.
The lower the ring number, the closer to the center the stone is.
If both teams' closest stone is the same distance from the center, no team scores.
Return:

A string in the format "team: number_of_points". e.g: "R: 2".
or "No points awarded" if neither team scored any points.
For example, given:

[
  [".", ".", "R", ".", "."],
  [".", "R", ".", ".", "."],
  ["Y", ".", ".", ".", "."],
  [".", "R", ".", ".", "."],
  [".", ".", ".", ".", "."]
]
Return "R: 2". The two red stones in ring 1 are tied for the closest and are the only two stones closer than yellows
closest.

1. score_curling([[".", ".", "R", ".", "."],
                  [".", "R", ".", ".", "."],
                  ["Y", ".", ".", ".", "."],
                  [".", "R", ".", ".", "."],
                  [".", ".", ".", ".", "."]])
    should return "R:2".
2. score_curling([[".", ".", "R", ".", "."],
                  [".", ".", ".", ".", "."],
                  [".", ".", "Y", ".", "R"],
                  [".", ".", "Y", "Y", "."],
                  [".", "Y", "R", "R", "."]])
    should return "Y: 3".
3. score_curling([[".", "R", "Y", ".", "."],
                  ["Y", ".", ".", ".", "."],
                  [".", ".", ".", ".", "."],
                  [".", "Y", "R", "Y", "."],
                  [".", ".", "R", "R", "."]])
    should return "No points awarded".
4. score_curling([[".", "Y", "Y", ".", "."],
                  ["Y", ".", ".", "R", "."],
                  [".", ".", "R", ".", "."],
                  [".", ".", "R", "R", "."],
                  [".", "Y", "R", "Y", "."]])
    should return "R: 4".
5. score_curling([["Y", "Y", "Y", "Y", "Y"],
                  ["Y", "R", "R", "R", "Y"],
                  ["Y", "R", "Y", "R", "Y"],
                  ["Y", "R", "R", "R", "Y"],
                  ["Y", "Y", "Y", "Y", "Y"]])
    should return "Y: 1".
6. score_curling([["Y", "R", "Y", "R", "Y"],
                  ["R", ".", ".", ".", "R"],
                  ["Y", ".", ".", ".", "Y"],
                  ["R", ".", ".", ".", "R"],
                  ["Y", ".", ".", "R", "Y"]])
    should return "No points awarded".
"""

def score_curling(house):
    red_rings = []
    yellow_rings = []

    for i in range(5):
        for j in range(5):
            if house[i][j] in ("R", "Y"):
                # Determine ring.
                if i == 2 and j == 2:
                    ring = 0
                elif abs(i - 2) <= 1 and abs(j - 2) <= 1:
                    ring = 1
                else:
                    ring = 2

                if house[i][j] == "R":
                    red_rings.append(ring)
                else:
                    yellow_rings.append(ring)

    # If one team has no stones.
    if not red_rings and not yellow_rings:
        return "No points awarded"
    if not red_rings:
        return "Y: " + str(len([r for r in yellow_rings if r < min(red_rings, default=3)]))
    if not yellow_rings:
        return "R: " + str(len([r for r in red_rings if r < min(yellow_rings, default=3)]))

    red_closest = min(red_rings)
    yellow_closest = min(yellow_rings)

    # Tie for closest.
    if red_closest == yellow_closest:
        return "No points awarded"

    if red_closest < yellow_closest:
        points = sum(1 for r in red_rings if r < yellow_closest)
        return f"R: {points}"
    else:
        points = sum(1 for r in yellow_rings if r < red_closest)
        return f"Y: {points}"


print(score_curling([[".", ".", "R", ".", "."],
                     [".", "R", ".", ".", "."],
                     ["Y", ".", ".", ".", "."],
                     [".", "R", ".", ".", "."],
                     [".", ".", ".", ".", "."]]))
print(score_curling([[".", ".", "R", ".", "."],
                     [".", ".", ".", ".", "."],
                     [".", ".", "Y", ".", "R"],
                     [".", ".", "Y", "Y", "."],
                     [".", "Y", "R", "R", "."]]))
print(score_curling([[".", "R", "Y", ".", "."],
                     ["Y", ".", ".", ".", "."],
                     [".", ".", ".", ".", "."],
                     [".", "Y", "R", "Y", "."],
                     [".", ".", "R", "R", "."]]))
print(score_curling([[".", "Y", "Y", ".", "."],
                     ["Y", ".", ".", "R", "."],
                     [".", ".", "R", ".", "."],
                     [".", ".", "R", "R", "."],
                     [".", "Y", "R", "Y", "."]]))
print(score_curling([["Y", "Y", "Y", "Y", "Y"],
                     ["Y", "R", "R", "R", "Y"],
                     ["Y", "R", "Y", "R", "Y"],
                     ["Y", "R", "R", "R", "Y"],
                     ["Y", "Y", "Y", "Y", "Y"]]))
print(score_curling([["Y", "R", "Y", "R", "Y"],
                     ["R", ".", ".", ".", "R"],
                     ["Y", ".", ".", ".", "Y"],
                     ["R", ".", ".", ".", "R"],
                     ["Y", ".", ".", "R", "Y"]]))
