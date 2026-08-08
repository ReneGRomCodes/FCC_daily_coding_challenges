/*
Nonogram Validator
Given an array of clue numbers and an array of cells, determine whether the cells satisfy the nonogram clue.

- The clue is an array of numbers representing the lengths of consecutive filled cells, in order. For example, a clue of
  [3, 2] means there should be 3 consecutive filled cells followed by 2 consecutive filled cells, separated by at least one empty cell.
- The row is an array of 1s (filled) and 0s (empty).

1. is_valid_nonogram([3, 2], [1, 1, 1, 0, 1, 1]) should return True.
2. is_valid_nonogram([3, 2], [0, 1, 1, 1, 1, 1]) should return False.
3. is_valid_nonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]) should return False.
4. is_valid_nonogram([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]) should return True.
5. is_valid_nonogram([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]) should return True.
6. is_valid_nonogram([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) should return False.
 */

function isValidNonogram(clue, cells) {
    const targetCells = [];
    const cleanedCells = [];

    // Populate 'targetCells' based on 'clue'.
    for (let i = 0; i < clue.length; i++) {
        for (let n = 0; n < clue[i]; n++) {
            targetCells.push(1);
        }
        if (i !== clue.length - 1) {
            targetCells.push(0);
        }
    }

    // Clean 'cells' to only have one 0 in between populated cells.
    for (let i = 0; i < cells.length; i++) {
        const m = cells[i];

        if (m === 0 && i !== 0 && cells[i - 1] !== 0 && i !== cells.length - 1) {
            cleanedCells.push(m);
        } else if (m === 1) {
            cleanedCells.push(m);
        }
    }

    // Drop trailing 0 that the previous loop didn't catch.
    if (cleanedCells[cleanedCells.length - 1] === 0) {
        cleanedCells.pop();
    }

    return targetCells.join("") === cleanedCells.join("");
}


console.log(isValidNonogram([3, 2], [1, 1, 1, 0, 1, 1]));
console.log(isValidNonogram([3, 2], [0, 1, 1, 1, 1, 1]));
console.log(isValidNonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]));
console.log(isValidNonogram([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]));
console.log(isValidNonogram([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]));
console.log(isValidNonogram([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]));
