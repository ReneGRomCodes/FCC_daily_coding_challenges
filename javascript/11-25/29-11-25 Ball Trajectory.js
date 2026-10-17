/*
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
 */

function getNextLocation(matrix) {
    const positions = {};  // Dict to store ball positions.

    for (let i = 0; i < matrix.length; i++) {
        for (const pos of matrix[i]) {
            if ([1, 2].includes(pos)) { positions[pos] = [i, matrix[i].indexOf(pos)] }
        }
    }

    // Compare positions to determine direction of movement and get next position.
    const [x1, x2] = [positions[1][0], positions[2][0]];
    const [y1, y2] = [positions[1][1], positions[2][1]];
    let [newX, newY] = [0, 0];

    if (x1 < x2) { newX = x2 + 1 }
    else if (x1 > x2) { newX = x2 - 1 }
    else { newX = x2 }

    if (y1 < y2) { newY = y2 + 1 }
    else if (y1 > y2) { newY = y2 - 1 }
    else { newY = y2 }

    // Check if new position is out of bounds, reverse movement (ball bounces) if so.
    if (newX < 0) { newX = 1 }
    if (newY < 0) { newY = 1 }
    if (newX > matrix[0].length - 1) { newX = x2 - 1 }
    if (newY > matrix.length - 1) { newY = y2 - 1 }

    return [newX, newY];
}


console.log(getNextLocation([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]));
console.log(getNextLocation([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]));
console.log(getNextLocation([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]));
console.log(getNextLocation([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]));
console.log(getNextLocation([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]));
