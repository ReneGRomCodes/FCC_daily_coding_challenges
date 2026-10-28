/*
Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".

1. count_permutations("abb") should return 3.
2. count_permutations("abc") should return 6.
3. count_permutations("racecar") should return 630.
4. count_permutations("freecodecamp") should return 39916800.
 */

function countPermutations(str) {
    // Simple factorial.
    function factorial(n) {
        let r = 1;
        for (let i = 2; i <= n; i++) {
            r *= i;
        }
        return r;
    }

    // Frequency count.
    const frequency = {};
    for (const char of str) {
        frequency[char] = (frequency[char] || 0) + 1;
    }

    let count = factorial(str.length);
    for (const v of Object.values(frequency)) {
        count /= factorial(v);
    }

    return count;
}



console.log(countPermutations("abb"));
console.log(countPermutations("abc"));
console.log(countPermutations("racecar"));
console.log(countPermutations("freecodecamp"));
