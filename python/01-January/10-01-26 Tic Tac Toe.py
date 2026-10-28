"""
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
"""

def tic_tac_toe(board: list[list[str]]) -> str:
    # Check horizontal and vertical positions.
    for i in range(3):
        if len(set(board[i])) == 1:
            return f"{board[i][0]} wins"
        elif board[0][i] == board[1][i] == board[2][i]:
            return f"{board[0][i]} wins"

    # Check diagonal positions.
    center_element = board[1][1]
    if (center_element == board[0][2] == board[2][0]) or (center_element == board[0][0] == board[2][2]):
        return f"{center_element} wins"

    return "Draw"


print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]))
print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]))
print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))
print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))
