/*
Number Words
Given an integer from 0 to 99, return its English word representation.

- 0 returns "zero".
- Numbers 1-19 have unique names ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
- Multiples of 10 from 20-90 have their own names ("twenty", "thirty", ..., "eighty", "ninety").
- Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example "forty-two" and
  "fifty-three".

1. getNumberWords(0) should return "zero".
2. getNumberWords(10) should return "ten".
3. getNumberWords(19) should return "nineteen".
4. getNumberWords(30) should return "thirty".
5. getNumberWords(53) should return "fifty-three".
6. getNumberWords(7) should return "seven".
7. getNumberWords(12) should return "twelve".
8. getNumberWords(60) should return "sixty".
9. getNumberWords(67) should return "sixty-seven".
10. getNumberWords(98) should return "ninety-eight".
 */

function getNumberWords(n) {
    const numberWords = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    if (n <= 19 || n % 10 === 0) {
        return numberWords[n];
    } else {
        const nArr = String(n).split("");
        return `${numberWords[Number(nArr[0]) * 10]}-${numberWords[Number(nArr[1])]}`;
    }
}


console.log(getNumberWords(0));
console.log(getNumberWords(10));
console.log(getNumberWords(19));
console.log(getNumberWords(30));
console.log(getNumberWords(53));
console.log(getNumberWords(7));
console.log(getNumberWords(12));
console.log(getNumberWords(60));
console.log(getNumberWords(67));
console.log(getNumberWords(98));
