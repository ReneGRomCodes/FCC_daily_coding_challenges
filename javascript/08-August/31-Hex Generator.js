/*
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
 */

let seed = 1234567;

// Yes, I totally came up with this one myself and did not google a way to generate random numbers without imports ;)
function rand255() {
    seed = (Math.imul(seed, 1103515245) + 12345) & 0x7fffffff;
    return seed % 256;
}


function generateHex(color) {
    if (!["red", "green", "blue"].includes(color.toLowerCase())) return "Invalid color";

    const a = rand255();
    const b = rand255();

    if (color.toLowerCase() === "red") {
        return `FF${a.toString(16).toUpperCase().padStart(2, "0")}${b.toString(16).toUpperCase().padStart(2, "0")}`;
    } else if (color.toLowerCase() === "green") {
        return `${a.toString(16).toUpperCase().padStart(2, "0")}FF${b.toString(16).toUpperCase().padStart(2, "0")}`;
    } else {  // Blue.
        return `${a.toString(16).toUpperCase().padStart(2, "0")}${b.toString(16).toUpperCase().padStart(2, "0")}FF`;
    }
}


console.log(generateHex("yellow"));
console.log(generateHex("red"));
console.log(generateHex("red"));
console.log(generateHex("green"));
console.log(generateHex("green"));
console.log(generateHex("blue"));
console.log(generateHex("blue"));
