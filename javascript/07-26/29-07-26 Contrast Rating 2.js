/*
Contrast Rating 2
Given two relative luminance values and a boolean indicating whether the text is large, return the WCAG contrast rating
using the following method:

Calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker one. The
lighter one will always be the first argument.

Return the rating based on the contrast ratio using the following table:
Rating	Normal Text	    Large Text
"AAA"	7.0+	        4.5+
"AA"	4.5+	        3.0+
"Fail"	below 4.5	    below 3.0

1. get_contrast_rating(1.0, 0.0, False) should return "AAA".
2. get_contrast_rating(0.9015, 0.1364, False) should return "AA".
3. get_contrast_rating(0.8965, 0.1628, False) should return "Fail".
4. get_contrast_rating(0.7469, 0.0957, True) should return "AAA".
5. get_contrast_rating(0.7489, 0.2018, True) should return "AA".
 */

function getContrastRating(l1, l2, isLargeText) {
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

    const luminanceValues = [l1 + 0.05, l2 + 0.05];
    const contrastRatio = Math.max(...luminanceValues) / Math.min(...luminanceValues);
    const size = isLargeText ? "large" : "normal";

    for (const [k, v] of Object.entries(contrastRating[size])) {
        if (contrastRatio >= v) {
            return k;
        }
    }

    return "Fail";
}


console.log(getContrastRating(1.0, 0.0, false));
console.log(getContrastRating(0.9015, 0.1364, false));
console.log(getContrastRating(0.8965, 0.1628, false));
console.log(getContrastRating(0.7469, 0.0957, true));
console.log(getContrastRating(0.7489, 0.2018, true));
