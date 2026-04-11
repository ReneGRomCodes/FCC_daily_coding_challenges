"""
Rook and Bishop Attack
Given a string for the location of a rook on a chess board, and another for the location of a bishop, determine if one
piece can attack another.

A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to
top). It looks like this:

A8	B8	C8	D8	E8	F8	G8	H8
A7	B7	C7	D7	E7	F7	G7	H7
A6	B6	C6	D6	E6	F6	G6	H6
A5	B5	C5	D5	E5	F5	G5	H5
A4	B4	C4	D4	E4	F4	G4	H4
A3	B3	C3	D3	E3	F3	G3	H3
A2	B2	C2	D2	E2	F2	G2	H2
A1	B1	C1	D1	E1	F1	G1	H1

- Rooks can move as many squares as they want in a horizontal or vertical direction.
- Bishops can move as many squares as they want in any diagonal direction.
- One piece can attack another if it can move to the location of that piece.

Return:
- "rook" if the rook can attack the bishop.
- "bishop" if the bishop can attack the rook.
- "neither" if neither piece can attack one another.

1. rook_bishop_attack("A1", "A5") should return "rook".
2. rook_bishop_attack("C3", "F6") should return "bishop".
3. rook_bishop_attack("D4", "D7") should return "rook".
4. rook_bishop_attack("B7", "H1") should return "bishop".
5. rook_bishop_attack("B3", "C5") should return "neither".
6. rook_bishop_attack("G3", "E8") should return "neither".
"""

def rook_bishop_attack(rook: str, bishop: str) -> str:
    # Turn column and rows to integer values for each piece.
    rook_col, bishop_col = ord(rook[0]), ord(bishop[0])
    rook_row, bishop_row = int(rook[1]), int(bishop[1])

    if rook_col == bishop_col or rook_row == bishop_row:
        return "rook"
    elif abs(rook_col - bishop_col) == abs(rook_row - bishop_row):
        return "bishop"
    else:
        return "neither"


print(rook_bishop_attack("A1", "A5"))
print(rook_bishop_attack("C3", "F6"))
print(rook_bishop_attack("D4", "D7"))
print(rook_bishop_attack("B7", "H1"))
print(rook_bishop_attack("B3", "C5"))
print(rook_bishop_attack("G3", "E8"))
