"""
Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].

1. shift_array([1, 2, 3], 1) should return [2, 3, 1].
2. shift_array([1, 2, 3], -1) should return [3, 1, 2].
3. shift_array(["alpha", "bravo", "charlie"], 5) should return ["charlie", "alpha", "bravo"].
4. shift_array(["alpha", "bravo", "charlie"], -11) should return ["bravo", "charlie", "alpha"].
5. shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) should return [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].
"""

def shift_array(arr: list[str | int], n: int) -> list[str | int]:
    n = n % len(arr)

    return arr[n:] + arr[:n]


print(shift_array([1, 2, 3], 1))
print(shift_array([1, 2, 3], -1))
print(shift_array(["alpha", "bravo", "charlie"], 5))
print(shift_array(["alpha", "bravo", "charlie"], -11))
print(shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15))
