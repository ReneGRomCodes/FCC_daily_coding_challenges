/*
Largest Number
Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").

1. largest_number("1,2") should return 2.
2. largest_number("4;15:60,26?52!0") should return 60.
3. largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011") should return -402.
4. largest_number("12;-50,99.9,49.1!-10.1?88?16") should return 99.9.
 */

function largestNumber(str) {
    const numbers = str.split(/[,!?:;]/)

    return Math.max(...numbers);
}


console.log(largestNumber("1,2"));
console.log(largestNumber("4;15:60,26?52!0"));
console.log(largestNumber("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011"));
console.log(largestNumber("12;-50,99.9,49.1!-10.1?88?16"));
