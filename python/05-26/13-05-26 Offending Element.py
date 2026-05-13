"""
Offending Element
Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.

If more than one element could be considered out of place, return the index of the first one.

1. find_offender([1, 6, 2, 3, 4, 5]) should return 1.
2. find_offender([1, 2, 3, 5, 4, 5]) should return 3.
3. find_offender([2, 1]) should return 0.
4. find_offender([2, 4, 1, 6, 8]) should return 2.
5. find_offender([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]) should return 6.
"""

def find_offender(arr: list[int]) -> int | None:

    for i, n in enumerate(arr):
        prev_ok: bool = (i == 0 or arr[i - 1] <= n)
        next_ok: bool = (i == len(arr) - 1 or n <= arr[i + 1])

        if not prev_ok or not next_ok:
            if i == 0 or i == len(arr) - 1:
                return i
            elif n > arr[i + 1] and arr[i - 1] > arr[i + 1]:
                return i + 1

            return i


print(find_offender([1, 6, 2, 3, 4, 5]))
print(find_offender([1, 2, 3, 5, 4, 5]))
print(find_offender([2, 1]))
print(find_offender([2, 4, 1, 6, 8]))
print(find_offender([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]))
