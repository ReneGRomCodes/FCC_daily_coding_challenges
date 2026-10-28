/*
ISBN-13 Validator
Given a string, determine if it is a valid ISBN-13 number.

A valid ISBN-13:
- Contains only digits and hyphens
- Has exactly 13 digits after removing hyphens
- Passes the following check:
    - Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second by 3, the third by 1, and so on).
    - The sum of the results must be divisible by 10.

1. is_valid_isbn_13("9780306406157") should return True.
2. is_valid_isbn_13("97803064061570") should return False.
3. is_valid_isbn_13("978-0-13-595705-9") should return True.
4. is_valid_isbn_13("978-030-64061A-4") should return False.
5. is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9") should return True.
 */

function isValidIsbn13(str) {
    const numbers = "0123456789";
    const cleanedStr = str.split("-").join("");
    let checksum = 0;

    if (cleanedStr.length !== 13) {
        return false;
    }

    for (let i = 1; i <= cleanedStr.length; i++) {
        const char = cleanedStr[i-1];

        if (!numbers.includes(char)) {
            return false;
        }

        const digit = Number(char)
        checksum += (i % 2 === 0) ? digit * 3 : digit;
    }

    return checksum % 10 === 0;
}


console.log(isValidIsbn13("9780306406157"));
console.log(isValidIsbn13("97803064061570"));
console.log(isValidIsbn13("978-0-13-595705-9"));
console.log(isValidIsbn13("978-030-64061A-4"));
console.log(isValidIsbn13("9-7-8-0-1-3-4-7-5-7-5-9-9"));
