/*
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
 */

function rgbToHex(rgb) {
    let hexadecimal = "#";
    rgb = rgb.slice(4, rgb.length - 1).split(", ");  // Extract RGB values as list of strings from 'rgb'.

    for (const v of rgb) {
        hexadecimal += parseInt(v).toString(16).padStart(2, "0");
    }

    return hexadecimal;
}


console.log(rgbToHex("rgb(255, 255, 255)"));
console.log(rgbToHex("rgb(1, 11, 111)"));
console.log(rgbToHex("rgb(173, 216, 230)"));
console.log(rgbToHex("rgb(79, 123, 201)"));
