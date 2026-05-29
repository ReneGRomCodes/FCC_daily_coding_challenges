"""
Wider Aspect Ratio
Given two strings for different image dimensions, return the aspect ratio of the image with a greater width-to-height
ratio.

- The given strings will be in the format "WxH", for example, "1920x1080".
- The aspect ratio is the ratio of width to height, reduced to the lowest whole numbers. For example, "1920x1080" reduces
  to "16:9".
- Return a string in format "W:H", for example, "16:9".

1. get_wider_aspect_ratio("1920x1080", "800x600") should return "16:9".
2. get_wider_aspect_ratio("1080x1350", "2048x1536") should return "4:3".
3. get_wider_aspect_ratio("640x480", "2440x1220") should return "2:1".
4. get_wider_aspect_ratio("360x640", "1080x1920") should return "9:16".
5. get_wider_aspect_ratio("3440x1440", "2048x858") should return "43:18".
6. get_wider_aspect_ratio("12345x61234", "12534x51234") should return "2089:8539".
"""

import math


def get_width_height(w, h):
    return int(w / math.gcd(w, h)), int(h / math.gcd(w, h))


def get_wider_aspect_ratio(a: str, b: str) -> str:
    a_width, a_height= int(a.split("x")[0]), int(a.split("x")[1])
    b_width, b_height = int(b.split("x")[0]), int(b.split("x")[1])

    if a_width / a_height > b_width / b_height:
        width, height = get_width_height(a_width, a_height)
    else:
        width, height = get_width_height(b_width, b_height)

    return f"{width}:{height}"


print(get_wider_aspect_ratio("1920x1080", "800x600"))
print(get_wider_aspect_ratio("1080x1350", "2048x1536"))
print(get_wider_aspect_ratio("640x480", "2440x1220"))
print(get_wider_aspect_ratio("360x640", "1080x1920"))
print(get_wider_aspect_ratio("3440x1440", "2048x858"))
print(get_wider_aspect_ratio("12345x61234", "12534x51234"))
