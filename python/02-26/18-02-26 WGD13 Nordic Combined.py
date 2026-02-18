"""
2026 Winter Games Day 13: Nordic Combined
Given an array of jump scores for athletes, calculate their start delay times for the cross-country portion of the Nordic
Combined.

The athlete with the highest jump score starts first (0 second delay). All other athletes start later based on how far
behind their jump score is compared to the best jump.

To calculate the delay for each athlete, subtract the athlete's jump score from the best overall jump score and multiply
the result by 1.5. Round the delay up to the nearest integer.

1. calculate_start_delays([120, 110, 125]) should return [8, 23, 0].
2. calculate_start_delays([118, 125, 122, 120]) should return [11, 0, 5, 8].
3. calculate_start_delays([100, 105, 95, 110, 120, 115, 108]) should return [30, 23, 38, 15, 0, 8, 18].
4. calculate_start_delays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124]) should return [3, 11, 6, 18, 21, 15, 8, 26, 0, 12].
"""
import math

def calculate_start_delays(jump_scores: list[int]) -> list[int]:
    return [math.ceil((max(jump_scores) - x) * 1.5) for x in jump_scores]


print(calculate_start_delays([120, 110, 125]))
print(calculate_start_delays([118, 125, 122, 120]))
print(calculate_start_delays([100, 105, 95, 110, 120, 115, 108]))
print(calculate_start_delays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124]))
