"""
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
"""

def decode(s: str) -> str:
    stack: list[str] = []

    for char in s:
        if char == ")":
            # Pop everything until the last "(".
            temp = []
            while stack and stack[-1] != "(":
                temp.append(stack.pop())
            stack.pop()  # Remove the "(".
            # Add reversed content back to stack.
            stack.extend(temp)
        else:
            stack.append(char)

    return "".join(stack)


print(decode("(f(b(dc)e)a)"))
print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
print(decode("f(Ce(re))o((e(aC)m)d)p"))
