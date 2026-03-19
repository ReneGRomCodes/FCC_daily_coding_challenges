/*
Inverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one
value are swapped with the other.

For example, given:
[
    ["a", "b"],
    ["a", "a"]
]

Return:
[
    ["b", "a"],
    ["b", "b"]
]

1. invert_matrix([["a", "b"], ["a", "a"]]) should return [["b", "a"], ["b", "b"]].
2. invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]) should return [[0, 1, 0], [0, 0, 0], [1, 0, 1]].
3. invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]])
    should return [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]].
4. invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]])
    should return [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]].
5. invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]])
    should return [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]].
 */

function invertMatrix(matrix) {
    let values = [];
    let invertedMatrix = [];

    for (let item of matrix) {
        values = [...new Set(item)];

        if (values.length === 2) {
            break;
        }
    }

    for (let item of matrix) {
        let invertedItem = [];

        for (let value of item) {
            if (value === values[0]) {
                invertedItem.push(values[1]);
            } else {
                invertedItem.push(values[0]);
            }
        }
        invertedMatrix.push(invertedItem);
    }

    return invertedMatrix;
}


console.log(invertMatrix([["a", "b"], ["a", "a"]]));
console.log(invertMatrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]));
console.log(invertMatrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]));
console.log(invertMatrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]));
console.log(invertMatrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]));
