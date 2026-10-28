/*
ISBN-10 Validator
Given a string, determine if it's a valid ISBN-10.

An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):
- The first 9 characters must be digits, and
- The final character may be a digit or the letter "X", which represents the number 10.

To validate it:
- Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
- Add all the results together.
- If the total is divisible by 11, it's valid.

1. is_valid_isbn10("0-306-40615-2") should return True.
2. is_valid_isbn10("0-306-40615-1") should return False.
3. is_valid_isbn10("0-8044-2957-X") should return True.
4. is_valid_isbn10("X-306-40615-2") should return False.
5. is_valid_isbn10("0-6822-2589-4") should return True.
 */

function isValidIsbn10(str) {
    const digits = "0123456789";
    const cleanedStr = str.split("-").join("");
    let digitSum = 0;

    if (cleanedStr.length !== 10) {
        return false;
    }

    for (let i = 1; i <= cleanedStr.length; i++) {
        let char = cleanedStr[i - 1];

        if (char === "X" && i !== 10) {  // 'X' is only allowed in last position.
            return false;

        } else {
            if (digits.includes(char)) {
                digitSum += Number(char) * i;
            } else if (char === "X") {
                digitSum += 10 * i;  // 'X' has value of 10 when in last position.
            } else {
                return false;
            }
        }
    }

    return digitSum % 11 === 0;
}


console.log(isValidIsbn10("0-306-40615-2"));
console.log(isValidIsbn10("0-306-40615-1"));
console.log(isValidIsbn10("0-8044-2957-X"));
console.log(isValidIsbn10("X-306-40615-2"));
console.log(isValidIsbn10("0-6822-2589-4"));
