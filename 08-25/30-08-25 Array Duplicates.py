"""
Array Duplicates
Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in
ascending order. If no values appear more than once, return an empty array.

Only include one instance of each value in the returned array.
1. find_duplicates([1, 2, 3, 4, 5]) should return [].
2. find_duplicates([1, 2, 3, 4, 1, 2]) should return [1, 2].
3. find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4])
    should return [-6, 0, 2, 4, 5, 23].
"""

def find_duplicates(arr: list[int]) -> list[int]:
    check_set: set = set()
    n_duplicates: list[int] = []

    for n in arr:
        if n not in check_set:
            check_set.add(n)
        elif n not in n_duplicates:
            n_duplicates.append(n)

    n_duplicates.sort()

    return n_duplicates


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 2, 3, 4, 1, 2]))
print(find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]))
