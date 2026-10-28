/*
Hex Validator
Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

Start with a #, and
be followed by either 3 or 6 hexadecimal characters.
Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).

1. is_valid_hex("#123") should return True.
2. is_valid_hex("#123abc") should return True.
3. is_valid_hex("#ABCDEF") should return True.
4. is_valid_hex("#0a1B2c") should return True.
5. is_valid_hex("#12G") should return False.
6. is_valid_hex("#1234567") should return False.
7. is_valid_hex("#12 3") should return False.
8. is_valid_hex("fff") should return False.
 */

function isValidHex(str) {
    const validChars = "abcdef0123456789";

    if (str[0] !== "#") {
        return false;
    } else if (![3, 6].includes(str.slice(1).length)) {
        return false;
    }

    for (const char of str.slice(1)) {
        if (!validChars.includes(char.toLowerCase())) {
            return false
        }
    }

    return true;
}


console.log(isValidHex("#123"));
console.log(isValidHex("#123abc"));
console.log(isValidHex("#ABCDEF"));
console.log(isValidHex("#0a1B2c"));
console.log(isValidHex("#12G"));
console.log(isValidHex("#1234567"));
console.log(isValidHex("#12 3"));
console.log(isValidHex("fff"));
