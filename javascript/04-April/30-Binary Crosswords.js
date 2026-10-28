/*
Binary Crossword

Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or
vertically in either direction:

0 1 0 0 0 0 0 1
0 1 1 0 1 1 1 1
0 1 0 0 0 1 0 0
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0
0 1 0 1 0 1 0 0
0 1 1 0 1 0 0 0
1 0 1 0 1 1 1 0

For example, "A" has the binary representation 01000001, which appears in the first row from left to right.

1. isInCrossword("I") should return true.
2. isInCrossword("D") should return true.
3. isInCrossword("0") should return true.
4. isInCrossword("u") should return true.
5. isInCrossword("Y") should return false.
6. isInCrossword("p") should return false.
7. isInCrossword("1") should return false.
8. isInCrossword("Q") should return false.
 */

const getRotatedGrid = (grid) =>
    Array.from({ length: grid[0].length }, (_, col) =>
        grid.map(row => row[col]).join("")
    );

const checkGridForBinary = (binary, grid) =>
    grid.some(row =>
        row.includes(binary) || [...row].reverse().join("").includes(binary)
    );

function isInCrossword(char) {
    const binGrid = [
        "01000001",
        "01101111",
        "01000100",
        "01100101",
        "01010010",
        "01010100",
        "01101000",
        "10101110"
    ];

    const charBin = char.charCodeAt(0).toString(2).padStart(8, "0");

    const rotated = getRotatedGrid(binGrid);

    return (
        checkGridForBinary(charBin, binGrid) ||
        checkGridForBinary(charBin, rotated)
    );
}


console.log(isInCrossword("I"));
console.log(isInCrossword("D"));
console.log(isInCrossword("0"));
console.log(isInCrossword("u"));
console.log(isInCrossword("Y"));
console.log(isInCrossword("p"));
console.log(isInCrossword("1"));
console.log(isInCrossword("Q"));
