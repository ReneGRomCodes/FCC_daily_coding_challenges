"""
Targeted Sum
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value.
Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

The returned array should have the indices in ascending order.
1. find_target([2, 7, 11, 15], 9) should return [0, 1].
2. find_target([3, 2, 4, 5], 6) should return [1, 2].
3. find_target([1, 3, 5, 6, 7, 8], 15) should return [4, 5].
4. find_target([1, 3, 5, 7], 14) should return 'Target not found'.
"""

def find_target(arr: list[int], target: int) -> list[int] | str:
    for index1, n1 in enumerate(arr):

        for index2, n2 in enumerate(arr):
            if n1 + n2 == target and index1 != index2:
                output_arr = [index1, index2]

                return sorted(output_arr)

    return "Target not found"


print(find_target([2, 7, 11, 15], 9))
print(find_target([3, 2, 4, 5], 6))
print(find_target([1, 3, 5, 6, 7, 8], 15))
print(find_target([1, 3, 5, 7], 14))
