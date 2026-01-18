"""
Symmetric Difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.

1. difference([1, 2, 3], [3, 4, 5]) should return [1, 2, 4, 5].
2. difference(["a", "b"], ["c", "b"]) should return ["a", "c"].
3. difference([1, "a", 2], [2, "b", "a"]) should return [1, "b"].
4. difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [2, 4, 6, 8].
"""

def difference(arr1: list[str | int], arr2: list[str | int]) -> list[str | int]:
    diff_set: set[str | int] = set.difference(set(arr1), set(arr2)) | set.difference(set(arr2), set(arr1))
    diff_list: list[str | int] = []

    for item in arr1 + arr2:
        if item in diff_set: diff_list.append(item)

    return diff_list


print(difference([1, 2, 3], [3, 4, 5]))
print(difference(["a", "b"], ["c", "b"]))
print(difference([1, "a", 2], [2, "b", "a"]))
print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
