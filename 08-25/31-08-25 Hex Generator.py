"""
Hex Generator
Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function should return "Invalid color".
The function should return a random six-character hex color code where the input color value is greater than any of the
others.

Example of valid outputs for a given input:
Input	Output
"red"	"FF0000"
"green"	"00FF00"
"blue"	"0000FF"

1. generate_hex("yellow") should return "Invalid color".
2. generate_hex("red") should return a six-character string.
3. generate_hex("red") should return a valid six-character hex color code.
4. generate_hex("red") should return a valid hex color with a higher red value than other colors.
5. Calling generate_hex("red") twice should return two different hex color values where red is dominant.
6. Calling generate_hex("green") twice should return two different hex color values where green is dominant.
7. Calling generate_hex("blue") twice should return two different hex color values where blue is dominant.
"""

_seed = 1234567  # Simple PRNG seed.

def _rand255() -> int:
    """Yes, I totally came up with this one myself and did not google a way to generate random numbers without
    imports ;) """
    global _seed
    _seed = (_seed * 1103515245 + 12345) & 0x7fffffff
    return _seed % 256

def generate_hex(color: str) -> str:
    if color.lower() not in ("red", "green", "blue"):
        return "Invalid color"

    a: int = _rand255()
    b: int = _rand255()

    if color.lower() == "red":
        return f"FF{a:02X}{b:02X}"
    elif color.lower() == "green":
        return f"{a:02X}FF{b:02X}"
    else:  # Blue.
        return f"{a:02X}{b:02X}FF"


print(generate_hex("yellow"))
print(generate_hex("red"))
print(generate_hex("red"))
print(generate_hex("green"))
print(generate_hex("green"))
print(generate_hex("blue"))
print(generate_hex("blue"))
