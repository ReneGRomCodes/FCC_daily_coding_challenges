/*
Roman Numeral Parser
Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol	Value
I	    1
V	    5
X	    10
L	    50
C	    100
D	    500
M	    1000

Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise,
values are added.

1. parse_roman_numeral("III") should return 3.
2. parse_roman_numeral("IV") should return 4.
3. parse_roman_numeral("XXVI") should return 26.
4. parse_roman_numeral("XCIX") should return 99.
5. parse_roman_numeral("CDLX") should return 460.
6. parse_roman_numeral("DIV") should return 504.
7. parse_roman_numeral("MMXXV") should return 2025.
 */

function convertSingleNumeral(singleNumeral) {
    const conversionTable = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    }

    return conversionTable[singleNumeral];
}


function parseRomanNumeral(numeral) {
    const numerals = numeral.split("");
    let sumN = 0;

    for (let i = 0; i < numerals.length - 1; i++) {
        const convNum = convertSingleNumeral(numerals[i]);
        const convNextNum = convertSingleNumeral(numerals[i + 1]);

        convNum < convNextNum ? sumN -= convNum : sumN += convNum;
    }

    sumN += convertSingleNumeral(numerals[numerals.length - 1]);

    return sumN;
}


console.log(parseRomanNumeral("III"));
console.log(parseRomanNumeral("IV"));
console.log(parseRomanNumeral("XXVI"));
console.log(parseRomanNumeral("XCIX"));
console.log(parseRomanNumeral("CDLX"));
console.log(parseRomanNumeral("DIV"));
console.log(parseRomanNumeral("MMXXV"));
