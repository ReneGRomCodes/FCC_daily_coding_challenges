/*
Next Bingo Number
Given a bingo number, return the next bingo number sequentially.

A bingo number is a single letter followed by a number in its range according to this chart:

Letter	Number Range
"B"	    1-15
"I"	    16-30
"N"	    31-45
"G"	    46-60
"O"	    61-75

For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1".

1. get_next_bingo_number("B10") should return "B11".
2. get_next_bingo_number("N33") should return "N34".
3. get_next_bingo_number("I30") should return "N31".
4. get_next_bingo_number("G60") should return "O61".
5. get_next_bingo_number("O75") should return "B1".
 */

function getNextBingoNumber(n) {
    const number = parseInt(n.slice(1), 10);

    let next = number + 1;
    if (next > 75) next = 1;  // Wrap around if last bingo number is reached.

    const letters = ["B", "I", "N", "G", "O"];
    const letterIndex = Math.floor((next - 1) / 15);

    return letters[letterIndex] + next;
}


console.log(getNextBingoNumber("B10"));
console.log(getNextBingoNumber("N33"));
console.log(getNextBingoNumber("I30"));
console.log(getNextBingoNumber("G60"));
console.log(getNextBingoNumber("O75"));
