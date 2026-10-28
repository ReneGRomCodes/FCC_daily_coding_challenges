/*
Letters-Numbers
Given a string containing only letters and numbers, return a new string where a hyphen (-) is inserted every time the
string switches from a letter to a number, or a number to a letter.

1. separate_letters_and_numbers("ABC123") should return "ABC-123".
2. separate_letters_and_numbers("Route66") should return "Route-66.
3. separate_letters_and_numbers("H3LL0W0RLD") should return "H-3-LL-0-W-0-RLD".
4. separate_letters_and_numbers("a1b2c3d4") should return "a-1-b-2-c-3-d-4".
 */

function separateLettersAndNumbers(s) {
    return [...s].reduce((result, char, index, arr) => {
        if (index === 0) return char;

        const prev = arr[index - 1];

        const isLetter = /[a-zA-Z]/.test(char);
        const wasLetter = /[a-zA-Z]/.test(prev);

        const isNumber = /[0-9]/.test(char);
        const wasNumber = /[0-9]/.test(prev);

        if (
            (isLetter && !wasLetter) ||
            (isNumber && !wasNumber)
        ) {
            return result + "-" + char;
        }

        return result + char;
    }, "");
}



console.log(separateLettersAndNumbers("ABC123"));
console.log(separateLettersAndNumbers("Route66"));
console.log(separateLettersAndNumbers("H3LL0W0RLD"));
console.log(separateLettersAndNumbers("a1b2c3d4"));
