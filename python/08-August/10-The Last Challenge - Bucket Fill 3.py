"""
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
"""

def bucket_fill(grid: list[list[str]], target_color: str) -> int:
    """Fuck it! No clue what they meant by intermediate colour, so I vibe coded this one. Yes, I admit it, because this
    was just ridiculous... and I can blame ChatGPT for this shitshow of a code ;)"""
    rows = len(grid)
    cols = len(grid[0])

    start = tuple(
        color
        for row in grid
        for color in row
    )

    if all(color == target_color for color in start):
        return 0

    colors = set(start)
    colors.add(target_color)

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    queue = [(start, 0)]
    seen = {start}
    position = 0

    while position < len(queue):
        state, clicks = queue[position]
        position += 1

        # Turn the flat state back into a grid.
        current = [
            list(state[row * cols:(row + 1) * cols])
            for row in range(rows)
        ]

        # Find every connected region.
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue

                old_color = current[row][col]
                region = []
                stack = [(row, col)]
                visited.add((row, col))

                while stack:
                    r, c = stack.pop()
                    region.append((r, c))

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and current[nr][nc] == old_color
                        ):
                            visited.add((nr, nc))
                            stack.append((nr, nc))

                # Try changing this entire region to every useful colour.
                for new_color in colors:
                    if new_color == old_color:
                        continue

                    next_grid = [row[:] for row in current]

                    for r, c in region:
                        next_grid[r][c] = new_color

                    next_state = tuple(
                        color
                        for row in next_grid
                        for color in row
                    )

                    if next_state in seen:
                        continue

                    if all(color == target_color for color in next_state):
                        return clicks + 1

                    seen.add(next_state)
                    queue.append((next_state, clicks + 1))

    return 0


print(bucket_fill([["B", "B"], ["B", "B"]], "R"))
print(bucket_fill([["G", "G", "G"], ["G", "G", "G"], ["G", "G", "G"]], "G"))
print(bucket_fill([["P", "P", "Y"], ["Y", "P", "Y"], ["Y", "P", "P"]], "O"))
print(bucket_fill([["G", "Y", "C", "C"], ["Y", "Y", "Y", "B"], ["C", "Y", "B", "B"], ["C", "B", "B", "C"]], "R"))
print(bucket_fill([["G", "G", "O", "O"], ["G", "Y", "B", "Y"], ["B", "Y", "B", "Y"], ["B", "Y", "B", "Y"], ["G", "G", "G", "G"]], "P"))
print(bucket_fill([["R", "G", "R", "G"], ["R", "G", "R", "G"], ["B", "B", "B", "B"], ["B", "B", "B", "B"], ["R", "G", "R", "G"]], "Y"))
