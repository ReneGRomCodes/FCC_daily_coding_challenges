"""
Next Bingo Number
Given a bingo number, return the next bingo number sequentially.

A bingo number is a single letter followed by a number in its range according to this chart:

Letter	Number Range
"B"	    1-15
"I"	    16-30
"N"	    31-45
"G"	    46-60
"O"	    61-75

For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1".

1. get_next_bingo_number("B10") should return "B11".
2. get_next_bingo_number("N33") should return "N34".
3. get_next_bingo_number("I30") should return "N31".
4. get_next_bingo_number("G60") should return "O61".
5. get_next_bingo_number("O75") should return "B1".
"""

def get_next_bingo_number(n: str) -> str:
    n_split: tuple[str, int] = (n[0].upper(), int(n[1:]))
    ranges: dict[tuple[int, int], str] = {
        (1, 15): "B",
        (16, 30): "I",
        (31, 45): "N",
        (46, 60): "G",
        (61, 75): "O",
    }

    next_int: int = n_split[1] + 1

    if next_int > 75:  # Wrap around if last bingo number is reached.
        next_int = 1

    for k, v in ranges.items():
        if k[0] <= next_int <= k[1]:
            return v + str(next_int)

    return n


print(get_next_bingo_number("B10"))
print(get_next_bingo_number("N33"))
print(get_next_bingo_number("I30"))
print(get_next_bingo_number("G60"))
print(get_next_bingo_number("O75"))
