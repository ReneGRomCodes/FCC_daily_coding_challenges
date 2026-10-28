/*
Tic-Tac-Toe
Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

Each element in the given matrix is either an "X" or "O".
A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

"X wins" if player X has three in a row.
"O wins" if player O has three in a row.
"Draw" if no player has three in a row.

1. tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]) should return "X wins".
2. tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]) should return "O wins".
3. tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]) should return "Draw".
4. tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]) should return "O wins".
5. tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]) should return "X wins".
6. tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]) should return "Draw".
 */

function vowelCase(str) {
    const vowels = ["a", "e", "i", "o", "u"];
    const vowelsCaseArr = [];

    for (const char of str) {
        if (vowels.includes(char.toLowerCase())) { vowelsCaseArr.push(char.toUpperCase()) }
        else { vowelsCaseArr.push(char.toLowerCase()) }
    }

    return vowelsCaseArr.join("");
}


console.log(vowelCase("vowelcase"));
console.log(vowelCase("coding is fun"));
console.log(vowelCase("HELLO, world!"));
console.log(vowelCase("git cherry-pick"));
console.log(vowelCase("HEAD~1"));
