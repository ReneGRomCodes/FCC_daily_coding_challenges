/*
Roman Numeral Fixer
Given a string of malformed Roman numerals, return the value in standard Roman numeral notation.

The input will only use additive notation, so each symbol adds its value to the total. As a reminder, here are the
symbols and values:

Symbol	Value
"I"	    1
"V"	    5
"X"	    10
"L"	    50
"C"	    100
"D"	    500
"M"	    1000

When re-encoding, use the largest possible symbol at each step, using subtractive pairs ("IV", "IX", "XL", "XC", "CD",
"CM") where needed.

1. fix_numerals("XIIIII") should return "XV".
2. fix_numerals("IIIILX") should return "LXIV".
3. fix_numerals("XXVVVIIIII") should return "XL".
4. fix_numerals("MDCCLXXXXVIIII") should return "MDCCXCIX".
5. fix_numerals("IIIIVVVVXXXXLLLLCCDD") should return "MCDLXIV".
6. fix_numerals("ILCDMIVDIIXLCVCXDL") should return "MMCMLXXXIV".
 */

const VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

const ROMANMAP = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"]
]


function fixNumerals(str) {
    let total = str
        .split("")
        .reduce((sum, ch) => sum + VALUES[ch], 0);
    const result = [];

    for (const [value, symbol] of ROMANMAP) {
        while (total >= value) {
            result.push(symbol);
            total -= value;
        }
    }

    return result.join("");
}


console.log(fixNumerals("XIIIII"));
console.log(fixNumerals("IIIILX"));
console.log(fixNumerals("XXVVVIIIII"));
console.log(fixNumerals("MDCCLXXXXVIIII"));
console.log(fixNumerals("IIIIVVVVXXXXLLLLCCDD"));
console.log(fixNumerals("ILCDMIVDIIXLCVCXDL"));
