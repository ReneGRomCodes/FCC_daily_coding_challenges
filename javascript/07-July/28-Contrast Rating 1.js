/*
Contrast Rating 1
Given a contrast ratio and a boolean indicating whether the text is large, return the WCAG rating using the following
table:

Rating	    Normal Text	    Large Text
"AAA"	    7.0+	        4.5+
"AA"	    4.5+	        3.0+
"Fail"	    below 4.5	    below 3.0

1. getContrastRating("7.5", false) should return "AAA".
2. getContrastRating("4.8", false) should return "AA".
3. getContrastRating("4.2", false) should return "Fail".
4. getContrastRating("4.5", true) should return "AAA".
5. getContrastRating("3.0", true) should return "AA".
6. getContrastRating("2.7", false) should return "Fail".
 */

function getContrastRating(ratio, isLargeText) {
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
    const size = isLargeText ? "large" : "normal";

    for (const [k, v] of Object.entries(contrastRating[size])) {
        if (ratio >= v) {
            return k;
        }
    }

    return "Fail";
}


console.log(getContrastRating("7.5", false));
console.log(getContrastRating("4.8", false));
console.log(getContrastRating("4.2", false));
console.log(getContrastRating("4.5", true));
console.log(getContrastRating("3.0", true));
console.log(getContrastRating("2.7", false));
