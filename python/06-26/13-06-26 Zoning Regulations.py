"""
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
"""

def get_zone_violations(grid: list[list[str]]) -> list[list[int]]:
    restrictions: dict[str, set[str]] = {
        "i": {"R", "I"},
        "A": {"C"},
        "R": {"i", "C"},
        "I": {"i"},
        "C": {"R", "A"},
    }
    violating_cells: list[list[int]] = []

    rows: int = len(grid)
    cols: int = len(grid[0])

    directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(rows):
        for j in range(cols):
            current_cell: str = grid[i][j]

            if current_cell not in restrictions:
                continue

            cell_restrictions = restrictions[current_cell]
            is_violating: bool = False

            for delta_i, delta_j in directions:
                next_i, next_j = i + delta_i, j + delta_j

                if 0 <= next_i < rows and 0 <= next_j < cols:
                    neighbor_cell: str = grid[next_i][next_j]

                    if neighbor_cell in cell_restrictions:
                        is_violating = True
                        break

            if is_violating:
                violating_cells.append([i, j])

    return violating_cells


print(get_zone_violations([["R", "C"], ["", "C"]]))
print(get_zone_violations([["", "i"], ["", "R"], ["R", "I"]]))
print(get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]))
print(get_zone_violations([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]]))
print(get_zone_violations([["R", "A", "A", "", "i", "i"], ["R", "I", "", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]]))
