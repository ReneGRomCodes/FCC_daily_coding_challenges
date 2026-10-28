"""
Flatten the Array
Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional
array. Retain the original order of the items in the arrays.

1. flatten([1, [2, 3], 4]) should return [1, 2, 3, 4].
2. flatten([5, [4, [3, 2]], 1]) should return [5, 4, 3, 2, 1].
3. flatten(["A", [[[["B"]]]], "C"]) should return ["A", "B", "C"].
4. flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]])
    should return ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"].
5. flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])
    should return ["red","blue","green","yellow","purple","orange","pink","brown"].
"""

def flatten(arr: list) -> list:
    result: list = []

    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))  # Recurse into sublist.
        else:
            result.append(item)  # Append non-list item.

    return result


print(flatten([1, [2, 3], 4]))
print(flatten([5, [4, [3, 2]], 1]))
print(flatten(["A", [[[["B"]]]], "C"]))
print(flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]))
print(flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]))
