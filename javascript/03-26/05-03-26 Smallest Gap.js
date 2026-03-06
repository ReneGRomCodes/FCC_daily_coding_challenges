/*
Smallest Gap
Given a string, return the substring between the two identical characters that have the smallest number of characters
between them (smallest gap).

There will always be at least one pair of matching characters.
The returned substring should exclude the matching characters.
If two or more gaps are the same length, return the characters from the first one.
For example, given "ABCDAC", return "DA".

Only "A" and "C" repeat in the string.
The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
So return the string between the two "C" characters.

1. smallest_gap("ABCDAC") should return "DA".
2. smallest_gap("racecar") should return "e".
3. smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4") should return "#q6e&rkf(p".
4. smallest_gap("Hello World") should return "".
5. smallest_gap("The quick brown fox jumps over the lazy dog.") should return "fox".
 */

function smallestGap(str) {
    const lastSeen = {};
    let minGap = Infinity;
    let result = "";

    for (let i = 0; i < str.length; i++) {
        const ch = str[i];

        if (ch in lastSeen) {
            const gap = i - lastSeen[ch] - 1;

            if (gap < minGap) {
                minGap = gap;
                result = str.slice(lastSeen[ch] + 1, i);
            }
        }

        lastSeen[ch] = i;
    }

    return result;
}


console.log(smallestGap("ABCDAC"));
console.log(smallestGap("racecar"));
console.log(smallestGap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"));
console.log(smallestGap("Hello World"));
console.log(smallestGap("The quick brown fox jumps over the lazy dog."));
