/*
Digits vs Letters
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than
digits, and "tie" if it has the same amount of digits and letters.

Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters.

1. digits_or_letters("abc123") should return "tie".
2. digits_or_letters("a1b2c3d") should return "letters".
3. digits_or_letters("1a2b3c4") should return "digits".
4. digits_or_letters("abc123!@#DEF") should return "letters".
5. digits_or_letters("H3110 W0R1D") should return "digits".
6. digits_or_letters("P455W0RD") should return "tie".
 */

function digitsOrLetters(str) {

    return str;
}


console.log(digitsOrLetters("abc123"));
console.log(digitsOrLetters("a1b2c3d"));
console.log(digitsOrLetters("1a2b3c4"));
console.log(digitsOrLetters("abc123!@#DEF"));
console.log(digitsOrLetters("H3110 W0R1D"));
console.log(digitsOrLetters("P455W0RD"));
