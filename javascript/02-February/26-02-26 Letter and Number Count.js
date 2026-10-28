/*
Letter and Number Count
Given a string, return a message with the count of how many letters and numbers it contains.

Letters are A-Z and a-z.
Numbers are 0-9.
Ignore all other characters.

Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers. If
either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead
of "1 numbers".

1. countLettersAndNumbers("helloworld123") should return "The string has 10 letters and 3 numbers.".
2. countLettersAndNumbers("Catch 22") should return "The string has 5 letters and 2 numbers.".
3. countLettersAndNumbers("A1!") should return "The string has 1 letter and 1 number.".
4. countLettersAndNumbers("12345") should return "The string has 0 letters and 5 numbers.".
5. countLettersAndNumbers("password") should return "The string has 8 letters and 0 numbers.".
 */

function countLettersAndNumbers(str) {
    let lettersN = 0;
    let numbersN = 0;

    for (let char of str) {
        if (/[a-zA-Z]/.test(char)) {
            lettersN++;
        } else if (/[0-9]/.test(char)) {
            numbersN++;
        }
    }

    const lettersS = `${lettersN} letter${lettersN !== 1 ? "s" : ""}`;
    const numbersS = `${numbersN} number${numbersN !== 1 ? "s" : ""}`;

    return `The string has ${lettersS} and ${numbersS}.`;
}


console.log(countLettersAndNumbers("helloworld123"));
console.log(countLettersAndNumbers("Catch 22"));
console.log(countLettersAndNumbers("A1!"));
console.log(countLettersAndNumbers("12345"));
console.log(countLettersAndNumbers("password"));
