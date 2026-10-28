"""
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
"""

def get_contrast_rating(ratio: str, is_large_text: bool) -> str:
    contrast_rating: dict[str, dict[str, float]] = {
        "normal": {
            "AAA": 7.0,
            "AA": 4.5,
        },
        "large": {
            "AAA": 4.5,
            "AA": 3.0,
        },
    }
    size, ratio = "large" if is_large_text else "normal", float(ratio)

    for k, v in contrast_rating[size].items():
        if ratio >= v:
            return k

    return "Fail"


print(get_contrast_rating("7.5", False))
print(get_contrast_rating("4.8", False))
print(get_contrast_rating("4.2", False))
print(get_contrast_rating("4.5", True))
print(get_contrast_rating("3.0", True))
print(get_contrast_rating("2.7", False))
