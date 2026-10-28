/*
QR Decoder
Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.

The QR code may be given in any rotation of 90 degree increments.
A correctly oriented code has a 2x2 group of 1's (orientation markers) in the bottom-left, top-left, and top-right corners.
The three 2x2 orientation markers are not part of the binary data.
The binary data is read left-to-right, top-to-bottom (like a book) when the QR code is correctly oriented.
A code will always have exactly one valid orientation.

For example, given:
[
  "110011",
  "110011",
  "000000",
  "000000",
  "110000",
  "110001"
]

or given the same code with a different orientation:
[
  "110011",
  "110011",
  "000000",
  "000000",
  "000011",
  "100011"
]

Return "000000000000000000000001", all the binary data excluding the three 2x2 orientation markers.

1. decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"]) should return "000000000000000000000001".
2. decode_qr(["100011", "000011", "000000", "000000", "110011", "110011"]) should return "000000000000000000000001".
3. decode_qr(["110011", "111111", "010000", "110000", "110011", "110100"]) should return "001101000011000000110100".
4. decode_qr(["011011", "101011", "101000", "100010", "110011", "111011"]) should return "010001000100010101010110".
5. decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"]) should return "010000100100100101001110".
 */

function decodeQr(qrCode) {

    // Rotate 90° clockwise.
    const rotate90 = matrix =>
        matrix[0].split('').map((_, c) =>
            matrix.map(row => row[c]).reverse().join('')
        );

    // Check for the 2x2 marker blocks in the correct corners.
    const hasMarkers = matrix => {
        const isBlock = (r, c) =>
            matrix[r][c] === '1' &&
            matrix[r][c+1] === '1' &&
            matrix[r+1][c] === '1' &&
            matrix[r+1][c+1] === '1';

        return isBlock(0, 0) &&  // top-left
            isBlock(0, 4) &&  // top-right
            isBlock(4, 0);    // bottom-left
    };

    // Extract all data bits except the 3 marker blocks.
    const extractData = matrix =>
        matrix.flatMap((row, r) =>
            row.split('').map((cell, c) =>
                !((r < 2 && c < 2) || (r < 2 && c >= 4) || (r >= 4 && c < 2)) ? cell : null
            ).filter(Boolean)
        ).join('');

    // Try all 4 rotations until correct orientation is found.
    for (let i = 0; i < 4; i++) {
        if (hasMarkers(qrCode)) return extractData(qrCode);
        qrCode = rotate90(qrCode);
    }

    return ''; // should never happen if input is valid.
}


console.log(decodeQr(["110011", "110011", "000000", "000000", "110000", "110001"]));
console.log(decodeQr(["100011", "000011", "000000", "000000", "110011", "110011"]));
console.log(decodeQr(["110011", "111111", "010000", "110000", "110011", "110100"]));
console.log(decodeQr(["011011", "101011", "101000", "100010", "110011", "111011"]));
console.log(decodeQr(["111100", "110001", "100011", "001101", "110011", "110011"]));
