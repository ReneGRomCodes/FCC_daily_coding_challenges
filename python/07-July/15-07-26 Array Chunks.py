"""
Array Chunks
Given an array and a chunk size, return the array split into sub-arrays of that size.

- The last chunk may be smaller if the array doesn't divide evenly.

1. chunk_array([1, 2, 3, 4, 5, 6], 3) should return [[1, 2, 3], [4, 5, 6]].
2. chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2) should return [[1, "two"], [3, "four"], [5, "six"], [7, "eight"]].
3. chunk_array([1, 2, 3, 4, 5], 3) should return [[1, 2, 3], [4, 5]].
4. chunk_array(["a", "b", "c", "d", "e"], 1) should return [["a"], ["b"], ["c"], ["d"], ["e"]].
5. chunk_array([1, 2, 3], 5) should return [[1, 2, 3]].
"""

def chunk_array(arr, chunk_size):
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]


print(chunk_array([1, 2, 3, 4, 5, 6], 3))
print(chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2))
print(chunk_array([1, 2, 3, 4, 5], 3))
print(chunk_array(["a", "b", "c", "d", "e"], 1))
print(chunk_array([1, 2, 3], 5))
