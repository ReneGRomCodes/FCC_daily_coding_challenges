/*
Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

- A palindrome is a string that is the same forward and backward.
- If it's not a palindrome, return "none".

1. palindrome_locator("racecar") should return "e".
2. palindrome_locator("level") should return "v".
3. palindrome_locator("freecodecamp") should return "none".
4. palindrome_locator("noon") should return "oo".
5. palindrome_locator("11100111") should return "00".
 */

function palindromeLocator(str) {
    if (str !== str.split("").reverse().join("")) {
        return "none";
    }

    const sLength = str.length;
    const centerIndex = Math.floor(sLength / 2);

    if (sLength % 2 === 0) {
        return str.slice(centerIndex - 1, centerIndex + 1);
    } else {
        return str.slice(centerIndex, centerIndex + 1);
    }
}


console.log(palindromeLocator("racecar"));
console.log(palindromeLocator("level"));
console.log(palindromeLocator("freecodecamp"));
console.log(palindromeLocator("noon"));
console.log(palindromeLocator("11100111"));
