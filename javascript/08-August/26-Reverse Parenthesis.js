/*
Reverse Parenthesis
Given a string that contains properly nested parentheses, return the decoded version of the string using the following
rules:

All characters inside each pair of parentheses should be reversed.
Parentheses should be removed from the final result.
If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the
reversal of the outer pair.
Assume all parentheses are evenly balanced and correctly nested.

1. decode("(f(b(dc)e)a)") should return "abcdef".
2. decode("((is?)(a(t d)h)e(n y( uo)r)aC)") should return "Can you read this?".
3. decode("f(Ce(re))o((e(aC)m)d)p") should return "freeCodeCamp".
 */

function decode(s) {
    const stack = [];

    for (const char of s) {
        if (char === ")") {
            // Pop everything until the last "(".
            const temp = [];
            while (stack && stack[stack.length-1] != "(") {
                temp.push(stack.pop());
            }
            stack.pop();  // Remove the "(".
            // Add reversed content back to stack.
            stack.push(...temp);
        } else {
            stack.push(char);
        }
    }

    return stack.join("");
}


console.log(decode("(f(b(dc)e)a)"));
console.log(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"));
console.log(decode("f(Ce(re))o((e(aC)m)d)p"));
