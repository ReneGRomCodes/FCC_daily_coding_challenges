"""
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
"""

def get_deepest_brackets(s: str) -> str:
    opening_brackets, closing_brackets = {"(", "[", "{"}, {")", "]", "}"}
    current_depth: int = 0
    max_depth: int = 0
    result: str = ""

    for char in s:
        if char in opening_brackets:
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
                result = ""

        elif char in closing_brackets:
            current_depth -= 1

        else:
            if current_depth == max_depth:
                result += char

    return result


print(get_deepest_brackets("(hello (world))"))
print(get_deepest_brackets("[outer [inner] outer]"))
print(get_deepest_brackets("{a{b}c{d{e}f}g}"))
print(get_deepest_brackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]"))
print(get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p"))
