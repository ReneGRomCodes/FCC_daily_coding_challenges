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

function ticTacToe(board) {
    // Check horizontal and vertical positions.
    for (let i = 0; i < 3; i++) {
        if (new Set(board[i]).size === 1) { return `${board[i][0]} wins` }
        else if (board[0][i] === board[1][i] && board[0][i] === board[2][i]) { return `${board[0][i]} wins` }
    }

    // Check diagonal positions.
    const centerElement = board[1][1];
    if (
        (centerElement === board[0][2] && board[0][2] === board[2][0]) ||
        (centerElement === board[0][0] && board[0][0] === board[2][2])
    ) {
        return `${centerElement} wins`
    }

    return "Draw";
}


console.log(ticTacToe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]));
console.log(ticTacToe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]));
console.log(ticTacToe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]));
console.log(ticTacToe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]));
console.log(ticTacToe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]));
console.log(ticTacToe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]));
