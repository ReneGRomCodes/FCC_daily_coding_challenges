"""
Between Two Buckets
Given two buckets of paint, each with an RGB color and a fullness level, return the mixed RGB color as an array of three
integers.

- Each bucket is an object (JavaScript) or dictionary (Python) with a color property (an array of three integers
  [r, g, b]) and a fullness property (0–100).
- The mixed color is a weighted average of each channel in the two colors based on fullness level, with each channel
  rounded to the nearest integer.

1. mix_paint({"color": [250, 250, 250], "fullness": 50}, {"color": [0, 0, 0], "fullness": 50}) should return [125, 125, 125].
2. mix_paint({"color": [250, 250, 250], "fullness": 80}, {"color": [0, 0, 0], "fullness": 20}) should return [200, 200, 200].
3. mix_paint({"color": [100, 150, 200], "fullness": 30}, {"color": [100, 150, 200], "fullness": 70}) should return [100, 150, 200].
4. mix_paint({"color": [143, 143, 101], "fullness": 45}, {"color": [100, 204, 204], "fullness": 90}) should return [114, 184, 170].
5. mix_paint({"color": [15, 134, 249], "fullness": 29}, {"color": [97, 178, 55], "fullness": 54}) should return [68, 163, 123].
"""

def mix_paint(bucket1: dict[str, list[int] | int], bucket2: dict[str, list[int] | int]) -> list[int]:
    mixed_color: list[int] = []

    for channel in range(3):
        weighted_average: int = round((bucket1["color"][channel] * bucket1["fullness"] +
                                       bucket2["color"][channel] * bucket2["fullness"]) /
                                      (bucket1["fullness"] + bucket2["fullness"]))
        mixed_color.append(weighted_average)

    return mixed_color


print(mix_paint({"color": [250, 250, 250], "fullness": 50}, {"color": [0, 0, 0], "fullness": 50}))
print(mix_paint({"color": [250, 250, 250], "fullness": 80}, {"color": [0, 0, 0], "fullness": 20}))
print(mix_paint({"color": [100, 150, 200], "fullness": 30}, {"color": [100, 150, 200], "fullness": 70}))
print(mix_paint({"color": [143, 143, 101], "fullness": 45}, {"color": [100, 204, 204], "fullness": 90}))
print(mix_paint({"color": [15, 134, 249], "fullness": 29}, {"color": [97, 178, 55], "fullness": 54}))
