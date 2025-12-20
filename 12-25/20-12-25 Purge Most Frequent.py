"""
Purge Most Frequent
Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

If multiple values are tied for most frequent, remove all of them.
Do not change any of the other elements or their order.

1. purge_most_frequent([1, 2, 2, 3]) should return [1, 3].
2. purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]) should return ["a", "b", "b", "c", "c", "c"].
3. purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]) should return ["red", "green", "red", "green"].
4. purge_most_frequent([5, 5, 5, 5]) should return [].
"""

def get_histogram(array: list[int | str]) -> dict[int | str, int]:
    histogram: dict[int | str, int] = {}

    for item in array:
        if item not in histogram:
            histogram[item] = 1
        else:
            histogram[item] += 1

    return histogram


def purge_most_frequent(arr: list[int | str]) -> list[int | str]:
    item_frequencies: dict[int | str, int] = get_histogram(arr)
    most_frequent: int | str = max(item_frequencies, key=item_frequencies.get)

    return [x for x in arr if x != most_frequent]


print(purge_most_frequent([1, 2, 2, 3]))
print(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]))
print(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]))
print(purge_most_frequent([5, 5, 5, 5]))
