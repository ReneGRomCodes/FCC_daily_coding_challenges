"""
Golden Ratio
Given two numbers, determine if their ratio approximates the golden ratio.

- Use a golden ratio of 1.618
- Allow a tolerance of 0.01

1. is_golden_ratio(21, 34) should return True.
2. is_golden_ratio(15, 20) should return False.
3. is_golden_ratio(8, 13) should return True.
4. is_golden_ratio(10, 16) should return False.
5. is_golden_ratio(1618, 1000) should return True.
6. is_golden_ratio(88, 55) should return False.
"""

def is_golden_ratio(a: int, b: int) -> bool:
    golden_ratio: float = 1.618
    tolerance: float = 0.01
    ratio_ab: float = max(a, b) / min(a, b)

    return abs(golden_ratio - ratio_ab) <= tolerance


print(is_golden_ratio(21, 34))
print(is_golden_ratio(15, 20))
print(is_golden_ratio(8, 13))
print(is_golden_ratio(10, 16))
print(is_golden_ratio(1618, 1000))
print(is_golden_ratio(88, 55))
