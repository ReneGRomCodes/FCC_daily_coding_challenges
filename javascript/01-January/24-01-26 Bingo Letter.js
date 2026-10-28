/*
Bingo! Letter
Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:

Letter	Number Range
"B"	    1-15
"I"	    16-30
"N"	    31-45
"G"	    46-60
"O"	    61-75

1. get_bingo_letter(75) should return "O".
2. get_bingo_letter(54) should return "G".
3. get_bingo_letter(25) should return "I".
4. get_bingo_letter(38) should return "N".
5. get_bingo_letter(11) should return "B".
 */

function getBingoLetter(n) {
    const bingoLetters = {
        "B": [1, 15],
        "I": [16, 30],
        "N": [31, 45],
        "G": [46, 60],
        "O": [61, 75],
    }

    for (const [letter, [min, max]] of Object.entries(bingoLetters)) {
        if (min <= n && n <= max) {
            return letter;
        }
    }
}


console.log(getBingoLetter(75));
console.log(getBingoLetter(54));
console.log(getBingoLetter(25));
console.log(getBingoLetter(38));
console.log(getBingoLetter(11));
