/*
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
 */

function isValidHSL(hsl) {
    const match = hsl.match(/^hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)\s*;?$/);
    if (!match) return false;

    const [h, s, l] = match.slice(1).map(Number);

    return h >= 0 && h <= 360 &&
        s >= 0 && s <= 100 &&
        l >= 0 && l <= 100;
}


console.log(isValidHSL("hsl(240, 50%, 50%)"));
console.log(isValidHSL("hsl( 200 , 50% , 75% )"));
console.log(isValidHSL("hsl(99,60%,80%);"));
console.log(isValidHSL("hsl(0, 0%, 0%) ;"));
console.log(isValidHSL("hsl(  10  ,  20%   ,  30%   )    ;"));
console.log(isValidHSL("hsl(361, 50%, 80%)"));
console.log(isValidHSL("hsl(300, 101%, 70%)"));
console.log(isValidHSL("hsl(200, 55%, 75)"));
console.log(isValidHSL("hsl (80, 20%, 10%)"));
