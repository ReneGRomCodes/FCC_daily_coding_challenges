"""
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
"""

def get_luminance(rgb: list[int]) -> float:
    new_rgb: list[float] = []

    for channel in rgb:
        channel: float = channel / 255

        if channel <= 0.04045:
            new_rgb.append(channel / 12.92)
        else:
            new_rgb.append(((channel + 0.055) / 1.055)**2.4)

    return 0.2126 * new_rgb[0] + 0.7152 * new_rgb[1] + 0.0722 * new_rgb[2]


def get_contrast_rating(rgb1: list[int], rgb2: list[int], is_large_text: bool) -> str:
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

    luminance_values: list[float] = [get_luminance(rgb1) + 0.05, get_luminance(rgb2) + 0.05]
    contrast_ratio: float = max(luminance_values) / min(luminance_values)
    size: str = "large" if is_large_text else "normal"

    for k, v in contrast_rating[size].items():
        if contrast_ratio >= v:
            return k

    return "Fail"


print(get_contrast_rating([255, 255, 255], [0, 0, 0], False))
print(get_contrast_rating([215, 188, 188], [55, 55, 55], False))
print(get_contrast_rating([143, 144, 210], [46, 47, 61], False))
print(get_contrast_rating([167, 167, 210], [53, 10, 53], True))
print(get_contrast_rating([135, 147, 155], [60, 70, 90], True))
print(get_contrast_rating([125, 210, 195], [105, 130, 90], True))
