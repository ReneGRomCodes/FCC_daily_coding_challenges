"""
Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1),
return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the balls hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.

1. get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) should return [2, 3].
2. get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) should return [3, 0].
3. get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) should return [1, 2].
4. get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) should return [1, 1].
5. get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) should return [2, 2].
"""

def get_next_location(matrix: list[list[int]]) -> list[int]:
    positions: dict[int, list[int]] = {}  # Dict to store ball positions.

    for index, row in enumerate(matrix):
        for pos in row:
            if pos in {1, 2}:
                positions[pos] = [index, row.index(pos)]

    # Compare positions to determine direction of movement and get next position.
    x_1, x_2 = positions[1][0], positions[2][0]
    y_1, y_2 = positions[1][1], positions[2][1]

    if x_1 < x_2:
        new_x = x_2 + 1
    elif x_1 > x_2:
        new_x = x_2 - 1
    else:
        new_x = x_2

    if y_1 < y_2:
        new_y = y_2 + 1
    elif y_1 > y_2:
        new_y = y_2 - 1
    else:
        new_y = y_2

    # Check if new position is out of bounds, reverse movement (ball bounces) if so.
    if new_x < 0:
        new_x = 1
    if new_y < 0:
        new_y = 1
    if new_x > len(matrix[0]) - 1:
        new_x = x_2 - 1
    if new_y > len(matrix) - 1:
        new_y = y_2 - 1

    return [new_x, new_y]


print(get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]))
print(get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]))
print(get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]))
print(get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]))
print(get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]))
