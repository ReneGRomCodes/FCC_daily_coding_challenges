"""
Array Sum
Given an array of numbers, return the sum of all the numbers.

1. sum_array([1, 2, 3, 4, 5]) should return 15.
2. sum_array([42]) should return 42.
3. sum_array([5, -2, 7, -3]) should return 7.
4. sum_array([203, 145, -129, 6293, 523, -919, 845, 2434]) should return 9395.
5. sum_array([0, 0]) should return 0.
"""

def sum_array(numbers: list[int]) -> int:
    return sum(numbers)


print(sum_array([1, 2, 3, 4, 5]))
print(sum_array([42]))
print(sum_array([5, -2, 7, -3]))
print(sum_array([203, 145, -129, 6293, 523, -919, 845, 2434]))
print(sum_array([0, 0]))
