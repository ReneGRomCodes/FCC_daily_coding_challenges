/*
Array Duplicates
Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in
ascending order. If no values appear more than once, return an empty array.

Only include one instance of each value in the returned array.
1. find_duplicates([1, 2, 3, 4, 5]) should return [].
2. find_duplicates([1, 2, 3, 4, 1, 2]) should return [1, 2].
3. find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4])
    should return [-6, 0, 2, 4, 5, 23].
 */

function findDuplicates(arr) {
    const checkSet = [];
    const nDuplicates = [];

    for (const n of arr) {
        if (!checkSet.includes(n)) {
            checkSet.push(n);
        } else if (!nDuplicates.includes(n)) {
            nDuplicates.push(n);
        }
    }

    return nDuplicates.sort((a, b) => a - b);
}


console.log(findDuplicates([1, 2, 3, 4, 5]));
console.log(findDuplicates([1, 2, 3, 4, 1, 2]));
console.log(findDuplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]));
