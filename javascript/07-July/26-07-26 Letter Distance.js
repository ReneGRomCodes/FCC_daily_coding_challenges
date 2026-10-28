/*
Letter Distance
Given two strings of equal length, return the sum of the shortest distances between each pair of characters.

- The input will only contain lowercase letters
- The alphabet is treated as a circle, so the distance between a and z is 1.

1. letter_distance("abc", "bcd") should return 3.
2. letter_distance("abc", "xyz") should return 9.
3. letter_distance("encrypt", "decrypt") should return 10.
4. letter_distance("algorithm", "codeblock") should return 43.
5. letter_distance("lobster", "penguin") should return 47.
6. letter_distance("alligator", "crocodile") should return 55.
 */

function letterDistance(str1, str2) {
    let total = 0;

    for (let i = 0; i < str1.length; i++) {
        const diff = Math.abs(
            str1.charCodeAt(i) - str2.charCodeAt(i)
        );

        total += Math.min(diff, 26 - diff);
    }

    return total;
}


console.log(letterDistance("abc", "bcd"));
console.log(letterDistance("abc", "xyz"));
console.log(letterDistance("encrypt", "decrypt"));
console.log(letterDistance("algorithm", "codeblock"));
console.log(letterDistance("lobster", "penguin"));
console.log(letterDistance("alligator", "crocodile"));
