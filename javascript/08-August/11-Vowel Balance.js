/*
Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels
in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.

1. is_balanced("racecar") should return True.
2. is_balanced("Lorem Ipsum") should return True.
3. is_balanced("Kitty Ipsum") should return False.
4. is_balanced("string") should return False.
5. is_balanced(" ") should return True.
6. is_balanced("abcdefghijklmnopqrstuvwxyz") should return False.
7. is_balanced("123A#b!E&*456-o.U") should return True.
 */

function isBalanced(s) {
    s = s.toLowerCase();
    const vowels = new Set(["a", "e", "i", "o", "u"]);
    const len = s.length;

    let center = Math.floor(len / 2);

    // ignore center character if odd.
    const left = s.slice(0, center);
    const right = s.slice(len % 2 === 0 ? center : center + 1);

    let countA = 0;
    let countB = 0;

    for (const ch of left) {
        if (vowels.has(ch)) countA++;
    }

    for (const ch of right) {
        if (vowels.has(ch)) countB++;
    }

    return countA === countB;
}


console.log(isBalanced("racecar"));
console.log(isBalanced("Lorem Ipsum"));
console.log(isBalanced("Kitty Ipsum"));
console.log(isBalanced("string"));
console.log(isBalanced(" "));
console.log(isBalanced("abcdefghijklmnopqrstuvwxyz"));
console.log(isBalanced("123A#b!E&*456-o.U"));
