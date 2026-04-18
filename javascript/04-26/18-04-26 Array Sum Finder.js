/*
Array Sum Finder
Given an array of numbers and a target number, return the first subset of two or more numbers that adds up to the target.

- The "first" subset is the one whose elements have the lowest possible indices, prioritizing the earliest index first.
- Each number in the array may only be used once.
- If no valid subset exists, return "Sum not found".

Return the matching numbers as an array in the order they appear in the original array.

1. find_sum([1, 3, 5, 7], 6) should return [1, 5].
2. find_sum([1, 2, 3, 4, 5], 5) should return [1, 4].
3. find_sum([1, 2, 3, 4, 5], 6) should return [1, 2, 3].
4. find_sum([-1, -2, 3, 4], 1) should return [-1, -2, 4].
5. find_sum([3, 1, 4, 1, 5, 9, 2, 6], 10) should return [3, 1, 4, 2].
6. find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 20) should return [1, 2, 3, 5, 9].
7. find_sum([7, 9, 4, 2, 5], 10) should return "Sum not found".
 */

function findSum(arr, target) {
    const n = arr.length;

    function backtrack(start, current, total) {
        // Valid subset: at least 2 elements.
        if (current.length >= 2 && total === target) {
            return [...current];
        }

        for (let i = start; i < n; i++) {
            current.push(arr[i]);
            const result = backtrack(i + 1, current, total + arr[i]);
            if (result) return result;
            current.pop();
        }

        return null;
    }

    const result = backtrack(0, [], 0);
    return result || "Sum not found";
}


console.log(findSum([1, 3, 5, 7], 6));
console.log(findSum([1, 2, 3, 4, 5], 5));
console.log(findSum([1, 2, 3, 4, 5], 6));
console.log(findSum([-1, -2, 3, 4], 1));
console.log(findSum([3, 1, 4, 1, 5, 9, 2, 6], 10));
console.log(findSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 20));
console.log(findSum([7, 9, 4, 2, 5], 10));
