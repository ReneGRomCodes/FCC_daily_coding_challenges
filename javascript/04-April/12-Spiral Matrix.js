/*
Spiral Matrix
Given a 2D matrix, return a flat array with all of its values in clockwise order.

The returned array should have the top-left value first, move right along the top row, then down the right column, then
left along the bottom row, then up the left column. Repeat inward for any remaining layers.

For example, given:
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

Return [1, 2, 3, 6, 9, 8, 7, 4, 5].

1. spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    should return [1, 2, 3, 6, 9, 8, 7, 4, 5].
2. spiral_matrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]])
    should return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"].
3. spiral_matrix([[True, False, False], [False, True, True], [False, True, False], [True, True, False]])
    should return [True, False, False, True, False, False, True, True, False, False, True, True].
4. spiral_matrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]])
    should return [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1].
 */

function spiralMatrix(matrix) {
    let top = 0;
    let bottom = matrix.length - 1;
    let left = 0;
    let right = matrix[0].length - 1;
    const result = [];

    while (top <= bottom && left <= right) {

        // 1. Go right (top row).
        for (let col = left; col <= right; col++) {
            result.push(matrix[top][col]);
        }
        top += 1;

        // 2. Go down (right column).
        for (let row = top; row <= bottom; row++) {
            result.push(matrix[row][right]);
        }
        right -= 1;

        // 3. Go left (bottom row).
        if (top <= bottom) {
            for (let col = right; col >= left; col--) {
                result.push(matrix[bottom][col]);
            }
            bottom -= 1;
        }

        // 4. Go up (left column).
        if (left <= right) {
            for (let row = bottom; row >= top; row--) {
                result.push(matrix[row][left]);
            }
            left += 1;
        }
    }

    return result;
}


console.log(spiralMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
console.log(spiralMatrix([["a", "b", "c", "d"], ["l", "m", "n", "e"], ["k", "p", "o", "f"], ["j", "i", "h", "g"]]));
console.log(spiralMatrix([[true, false, false], [false, true, true], [false, true, false], [true, true, false]]));
console.log(spiralMatrix([[25, 24, 23, 22, 21], [10, 9, 8, 7, 20], [11, 2, 1, 6, 19], [12, 3, 4, 5, 18], [13, 14, 15, 16, 17]]));
