/*
Bingo Range
Given a bingo letter, return the number range associated with that letter.

Letter	Number Range
"B"	    1-15
"I"	    16-30
"N"	    31-45
"G"	    46-60
"O"	    61-75

Return an array with all numbers in the range from smallest to largest.

1. get_bingo_range("B") should return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15].
2. get_bingo_range("I") should return [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30].
3. get_bingo_range("N") should return [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45].
4. get_bingo_range("G") should return [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60].
5. get_bingo_range("O") should return [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75].
 */

function getBingoRange(letter) {
    const ranges = {
        "B": [1, 15],
        "I": [16, 30],
        "N": [31, 45],
        "G": [46, 60],
        "O": [61, 75]
    };
    const bingoRange = [];
    const [start, end] = ranges[letter.toUpperCase()];

    for (let i = start; i <= end; i++) {
        bingoRange.push(i)
    }

    return bingoRange;
}


console.log(getBingoRange("B"));
console.log(getBingoRange("I"));
console.log(getBingoRange("N"));
console.log(getBingoRange("G"));
console.log(getBingoRange("O"));
