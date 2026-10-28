/*
Contrast Rating 3
Given two arrays representing RGB values and a boolean indicating whether the text is large, return the WCAG contrast
rating using the following method:

First, convert each RGB value to relative luminance:
- Divide each channel [R, G, B] by 255 to get a value between 0 and 1
- Apply the gamma correction formula to each channel:
  - If the channel value is less than or equal to 0.04045: channel / 12.92
  - Otherwise: ((channel + 0.055) / 1.055) ^ 2.4
- Calculate luminance: 0.2126 * R + 0.7152 * G + 0.0722 * B

Then, calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker
one. The lighter one will always be the first argument.

Return the rating based on the contrast ratio using the following table:
Rating	    Normal Text	    Large Text
"AAA"	    7.0+	        4.5+
"AA"	    4.5+	        3.0+
"Fail"	    below 4.5	    below 3.0

1. get_contrast_rating([255, 255, 255], [0, 0, 0], False) should return "AAA".
2. get_contrast_rating([215, 188, 188], [55, 55, 55], False) should return "AA".
3. get_contrast_rating([143, 144, 210], [46, 47, 61], False) should return "Fail".
4. get_contrast_rating([167, 167, 210], [53, 10, 53], True) should return "AAA".
5. get_contrast_rating([135, 147, 155], [60, 70, 90], True) should return "AA".
6. get_contrast_rating([125, 210, 195], [105, 130, 90], True) should return "Fail".
 */

function getLuminance(rgb) {
    const newRgb = [];

    for (let channel of rgb) {
        channel = channel / 255
        channel <= 0.04045 ? newRgb.push(channel / 12.92) : newRgb.push(((channel + 0.055) / 1.055) ** 2.4)
    }

    return 0.2126 * newRgb[0] + 0.7152 * newRgb[1] + 0.0722 * newRgb[2]
}


function getContrastRating(rgb1, rgb2, isLargeText) {
    const contrastRating = {
        "normal": {
            "AAA": 7.0,
            "AA": 4.5,
        },
        "large": {
            "AAA": 4.5,
            "AA": 3.0,
        },
    };

    const luminanceValues = [getLuminance(rgb1) + 0.05, getLuminance(rgb2) + 0.05];
    const contrastRatio = Math.max(...luminanceValues) / Math.min(...luminanceValues);
    const size = isLargeText ? "large" : "normal";

    for (const [k, v] of Object.entries(contrastRating[size])) {
        if (contrastRatio >= v) {
            return k;
        }
    }

    return "Fail";
}


console.log(getContrastRating([255, 255, 255], [0, 0, 0], false));
console.log(getContrastRating([215, 188, 188], [55, 55, 55], false));
console.log(getContrastRating([143, 144, 210], [46, 47, 61], false));
console.log(getContrastRating([167, 167, 210], [53, 10, 53], true));
console.log(getContrastRating([135, 147, 155], [60, 70, 90], true));
console.log(getContrastRating([125, 210, 195], [105, 130, 90], true));
