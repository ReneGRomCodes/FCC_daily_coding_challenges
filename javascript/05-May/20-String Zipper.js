/*
String Zipper
Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append
the remaining characters at the end.

Begin with the first character of the first string.

1. zip_strings("abc", "123") should return "a1b2c3".
2. zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz") should return "abcdefghijklmnopqrstuvwxyz".
3. zip_strings("day", "night") should return "dnaiyght".
4. zip_strings("python", "javascript") should return "pjyatvhaosncript".
5. zip_strings("feCdCm", "reoeap") should return "freeCodeCamp".
 */

function zipStrings(a, b) {
    let zipped = "";
    const minLength = Math.min(a.length, b.length);

    // Interleave up to the shorter string's limit.
    for (let i = 0; i < minLength; i++) {
        zipped += a[i] + b[i];
    }

    // Slap the remainders on the end (one of these will be empty).
    zipped += a.slice(minLength) + b.slice(minLength);

    return zipped;
}


console.log(zipStrings("abc", "123"));
console.log(zipStrings("acegikmoqsuwy", "bdfhjlnprtvxz"));
console.log(zipStrings("day", "night"));
console.log(zipStrings("python", "javascript"));
console.log(zipStrings("feCdCm", "reoeap"));
