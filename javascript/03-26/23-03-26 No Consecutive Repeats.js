/*
No Consecutive Repeats
Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.

1. has_no_repeats("hi world") should return True.
2. has_no_repeats("hello world") should return False.
3. has_no_repeats("abcdefghijklmnopqrstuvwxyz") should return True.
4. has_no_repeats("freeCodeCamp") should return False.
5. has_no_repeats("The quick brown fox jumped over the lazy dog.") should return True.
6. has_no_repeats("Mississippi") should return False.
 */

function hasNoRepeats(str) {
    for (let i = 0; i < str.length; i++) {
        if (i !== 0 && str[i] === str[i - 1]) {
            return false
        }
    }
    return true;
}


console.log(hasNoRepeats("hi world"));
console.log(hasNoRepeats("hello world"));
console.log(hasNoRepeats("abcdefghijklmnopqrstuvwxyz"));
console.log(hasNoRepeats("freeCodeCamp"));
console.log(hasNoRepeats("The quick brown fox jumped over the lazy dog."));
console.log(hasNoRepeats("Mississippi"));
