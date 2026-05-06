/*
Deepest Brackets
Given a string containing balanced brackets, return the content of the deepest nested brackets.

- Brackets can be any of the three types: (), [], and {}.
- The input will always have a single deepest group.

For example, given "(hello (world))", return "world".

1. getDeepestBrackets("(hello (world))") should return "world".
2. getDeepestBrackets("[outer [inner] outer]") should return "inner".
3. getDeepestBrackets("{a{b}c{d{e}f}g}") should return "e".
4. getDeepestBrackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]") should return "fox".
5. getDeepestBrackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p") should return "C".
 */

function getDeepestBrackets(str) {
    const openingBrackets = ["(", "[", "{"];
    const closingBrackets = [")", "]", "}"];
    let currentDepth = 0;
    let maxDepth = 0;
    let result = "";

    for (const char of str) {
        if (openingBrackets.includes(char)) {
            currentDepth += 1;
            if (currentDepth > maxDepth) {
                maxDepth = currentDepth;
                result = "";
            }
        } else if (closingBrackets.includes(char)) {
            currentDepth -= 1;
        } else {
            if (currentDepth === maxDepth) {
                result += char;
            }
        }
    }

    return result;
}


console.log(getDeepestBrackets("(hello (world))"));
console.log(getDeepestBrackets("[outer [inner] outer]"));
console.log(getDeepestBrackets("{a{b}c{d{e}f}g}"));
console.log(getDeepestBrackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]"));
console.log(getDeepestBrackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"));
