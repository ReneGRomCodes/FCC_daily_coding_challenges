/*
Last Letter
Given a string, return the letter from the string that appears last in the alphabet.

- If two or more letters tie for the last in the alphabet, return the first one.
- Ignore all non-letter characters.

1. get_last_letter("world") should return "w".
2. get_last_letter("Hello World") should return "W".
3. get_last_letter("The quick brown fox jumped over the lazy dog.") should return "z".
4. get_last_letter("HeLl0") should return "L".
5. get_last_letter("!#$ er@R asd fT.,> 2t0e9") should return "T".
 */

function getLastLetter(str) {
    let maxChar = '';
    let maxCharIndex;

    for (const c of str) {
        const lower = c.toLowerCase();
        if (lower >= 'a' && lower <= 'z' && lower > maxChar) {
            maxChar = lower;
        }
    }

    maxCharIndex = str.toLowerCase().indexOf(maxChar);

    return str[maxCharIndex];
}


console.log(getLastLetter("world"));
console.log(getLastLetter("Hello World"));
console.log(getLastLetter("The quick brown fox jumped over the lazy dog."));
console.log(getLastLetter("HeLl0"));
console.log(getLastLetter("!#$ er@R asd fT.,> 2t0e9"));
