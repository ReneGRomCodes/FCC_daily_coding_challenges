/*
Captured Chess Pieces
Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your
opponent has captured.

In chess, you start with 16 pieces:

Piece	Abbreviation	Quantity	Value
Pawn	"P"	            8	        1
Rook	"R"	            2	        5
Knight	"N"	            2	        3
Bishop	"B"	            2	        3
Queen	"Q"	            1	        9
King	"K"	            1	        0

The given array will only contain the abbreviations above.
Any of the 16 pieces not included in the given array have been captured.
Return the total value of all captured pieces, unless...
If the King has been captured, return "Checkmate".

1. get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]) should return 8.
2. get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]) should return 26.
3. get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]) should return 16.
4. get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]) should return 4.
5. get_captured_value(["P", "K"]) should return 38.
6. get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]) should return 0.
7. get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]) should return "Checkmate".
 */

const PIECES = {
    "P": {"Quantity": 8,
        "Value": 1},
    "R": {"Quantity": 2,
        "Value": 5},
    "N": {"Quantity": 2,
        "Value": 3},
    "B": {"Quantity": 2,
        "Value": 3},
    "Q": {"Quantity": 1,
        "Value": 9},
    "K": {"Quantity": 1,
        "Value": 0},
};

function getCapturedValue(pieces) {
    let captureValue = 0;

    if (!pieces.includes("K")) {
        return "Checkmate";
    }

    for (let piece in PIECES) {
        captureValue += PIECES[piece].Value * (PIECES[piece].Quantity - pieces.reduce((a, b) => a + (b === piece), 0));
    }

    return captureValue;
}


console.log(getCapturedValue(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]));
console.log(getCapturedValue(["P", "P", "P", "P", "P", "R", "B", "K"]));
console.log(getCapturedValue(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]));
console.log(getCapturedValue(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]));
console.log(getCapturedValue(["P", "K"]));
console.log(getCapturedValue(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]));
console.log(getCapturedValue(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]));
