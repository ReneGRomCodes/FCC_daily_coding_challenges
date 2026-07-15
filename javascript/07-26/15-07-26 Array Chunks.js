/*
Array Chunks
Given an array and a chunk size, return the array split into sub-arrays of that size.

- The last chunk may be smaller if the array doesn't divide evenly.

1. chunk_array([1, 2, 3, 4, 5, 6], 3) should return [[1, 2, 3], [4, 5, 6]].
2. chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2) should return [[1, "two"], [3, "four"], [5, "six"], [7, "eight"]].
3. chunk_array([1, 2, 3, 4, 5], 3) should return [[1, 2, 3], [4, 5]].
4. chunk_array(["a", "b", "c", "d", "e"], 1) should return [["a"], ["b"], ["c"], ["d"], ["e"]].
5. chunk_array([1, 2, 3], 5) should return [[1, 2, 3]].
 */

function chunkArray(arr, size) {
    const result = [];

    for (let i = 0; i < arr.length; i += size) {
        result.push(arr.slice(i, i + size));
    }

    return result;
}


console.log(chunkArray([1, 2, 3, 4, 5, 6], 3));
console.log(chunkArray([1, "two", 3, "four", 5, "six", 7, "eight"], 2));
console.log(chunkArray([1, 2, 3, 4, 5], 3));
console.log(chunkArray(["a", "b", "c", "d", "e"], 1));
console.log(chunkArray([1, 2, 3], 5));
