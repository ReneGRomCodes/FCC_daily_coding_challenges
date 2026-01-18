"""
RGB to Hex
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

Input	                Output
"rgb(255, 255, 255)"	"#ffffff"
"rgb(1, 2, 3)"	        "#010203"

Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.

1. rgb_to_hex("rgb(255, 255, 255)") should return "#ffffff".
2. rgb_to_hex("rgb(1, 11, 111)") should return "#010b6f".
3. rgb_to_hex("rgb(173, 216, 230)") should return "#add8e6".
4. rgb_to_hex("rgb(79, 123, 201)") should return "#4f7bc9".
"""

def rgb_to_hex(rgb: str) -> str:
    """Long solution using 'hex()' method and manual formatting of output string."""
    hexadecimal: str = "#"
    rgb: list[str] = rgb[4:-1].split(", ")  # Extract RGB values as list of strings from 'rgb'.

    for v in rgb:
        v_hex: str = hex(int(v))  # Returns hex value for int, but needs some formatting.

        # Format string output from 'hex()' method.
        x_index: int = 0

        for index, char in enumerate(v_hex):
            if char == "x":
                x_index = index
                break

        v_hex = v_hex[x_index+1:]

        if len(v_hex) == 1:
            v_hex = f"0{v_hex}"

        # Add formatted string output to return value.
        hexadecimal += v_hex

    return hexadecimal


def rgb_to_hex_short(rgb: str) -> str:
    """Shorter solution that just straight-up uses f"{int(v):02x}" to format the output."""
    hexadecimal: str = "#"
    rgb: list[str] = rgb[4:-1].split(", ")  # Extract RGB values as list of strings from 'rgb'.

    for v in rgb:
        hexadecimal += f"{int(v):02x}"

    return hexadecimal


print(rgb_to_hex("rgb(255, 255, 255)"))
print(rgb_to_hex("rgb(1, 11, 111)"))
print(rgb_to_hex("rgb(173, 216, 230)"))
print(rgb_to_hex("rgb(79, 123, 201)"))
