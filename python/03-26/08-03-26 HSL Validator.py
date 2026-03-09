"""
HSL Validator
Given a string, determine whether it is a valid CSS hsl() color value.

A valid HSL value must be in the format "hsl(h, s%, l%)", where:
- h (hue) must be a number between 0 and 360 (inclusive).
- s (saturation) must be a percentage between 0% and 100%.
- l (lightness) must be a percentage between 0% and 100%.

Spaces are only allowed:
- After the opening parenthesis
- Before and/or after the commas
- Before and/or after closing parenthesis

Optionally, the value can end with a semi-colon (";").

For example, "hsl(240, 50%, 50%)" is a valid HSL value.

1. is_valid_hsl("hsl(240, 50%, 50%)") should return True.
2. is_valid_hsl("hsl( 200 , 50% , 75% )") should return True.
3. is_valid_hsl("hsl(99,60%,80%);") should return True.
4. is_valid_hsl("hsl(0, 0%, 0%) ;") should return True.
5. is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;") should return True.
6. is_valid_hsl("hsl(361, 50%, 80%)") should return False.
7. is_valid_hsl("hsl(300, 101%, 70%)") should return False.
8. is_valid_hsl("hsl(200, 55%, 75)") should return False.
9. is_valid_hsl("hsl (80, 20%, 10%)") should return False.
"""

def is_valid_hsl(hsl: str) -> bool:
    # Extract and clean hsl-values.
    values: list[str] = hsl[hsl.index("(")+1:hsl.index(")")].split(",")

    for i, v in enumerate(values):
        values[i] = v.strip()

    # Check hsl-values for correct format and range.
    test_1 = values[1][-1] != "%" or values[2][-1] != "%"
    test_2 = not 0 <= int(values[0]) <= 360
    test_3 = not 0 <= int(values[1][:-1]) <= 100
    test_4 = not 0 <= int(values[2][:-1]) <= 100

    if any([test_1, test_2, test_3, test_4]):
        return False

    # Check allowed spaces.
    if " " in hsl[:hsl.index("(")]:
        return False

    tail = hsl[hsl.index(")") + 1:].strip()
    if tail not in ("", ";"):
        return False

    return True


print(is_valid_hsl("hsl(240, 50%, 50%)"))
print(is_valid_hsl("hsl( 200 , 50% , 75% )"))
print(is_valid_hsl("hsl(99,60%,80%);"))
print(is_valid_hsl("hsl(0, 0%, 0%) ;"))
print(is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;"))
print(is_valid_hsl("hsl(361, 50%, 80%)"))
print(is_valid_hsl("hsl(300, 101%, 70%)"))
print(is_valid_hsl("hsl(200, 55%, 75)"))
print(is_valid_hsl("hsl (80, 20%, 10%)"))
