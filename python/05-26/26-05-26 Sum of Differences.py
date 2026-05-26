"""
Sum of Differences
Given an array of numbers, return the sum of the differences between each number and the one that follows it.

For example, given [1, 3, 4], return 3 (2 + 1).

1. sum_of_differences([1, 3, 4]) should return 3.
2. sum_of_differences([5, -3, 3, 9, 10]) should return 5.
3. sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7]) should return -16.
4. sum_of_differences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75]) should return 25.
"""

def sum_of_differences(arr: list[int]) -> int:
    return arr[-1] - arr[0]


print(sum_of_differences([1, 3, 4]))
print(sum_of_differences([5, -3, 3, 9, 10]))
print(sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7]))
print(sum_of_differences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75]))
