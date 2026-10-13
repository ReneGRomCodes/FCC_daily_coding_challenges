"""
100 Characters
Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100
characters, trim the extra so it's exactly 100.

1. one_hundred("One hundred ")
    should return "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ".
2. one_hundred("freeCodeCamp ")
    should return "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC".
3. one_hundred("daily challenges ")
    should return "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge".
4. one_hundred("!")
    should return "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".
"""

def one_hundred(chars: str) -> str:
    output: list[str] = []
    length: int = 0

    while length < 100:
        output.append(chars)
        length += 1

    return "".join(output)[:100]


print(one_hundred("One hundred "))
print(one_hundred("freeCodeCamp "))
print(one_hundred("daily challenges "))
print(one_hundred("!"))
