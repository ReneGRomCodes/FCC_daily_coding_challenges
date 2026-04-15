/*
Sorted Array Swap
Given an array of integers, return a new array using the following rules:

- Sort the integers in ascending order
- Then swap all values whose index is a multiple of 3 with the value before it.

1. sort_and_swap([3, 1, 2, 4, 6, 5]) should return [1, 2, 4, 3, 5, 6].
2. sort_and_swap([9, 7, 5, 3, 1, 2, 4, 6, 8]) should return [1, 2, 4, 3, 5, 7, 6, 8, 9].
3. sort_and_swap([1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [1, 2, 4, 3, 5, 7, 6, 8, 9].
4. sort_and_swap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]) should return [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 12].
5. sort_and_swap([100, -50, 0, 75, -25, 50, -75, 25]) should return [-75, -50, 0, -25, 25, 75, 50, 100].
6. sort_and_swap([5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2])
    should return [-65, -10, 0, -4, 2, 8, 5, 9, 77, 13, 88, 101, 99, 313].
 */

function sortAndSwap(arr) {
    const sortedArr = arr.sort((a, b) => a - b);
    const newArr = [];

    for (let i = 0; i < sortedArr.length; i++) {
        if (i % 3 === 0) {
            newArr.splice(i - 1, 0, sortedArr[i])
        } else {
            newArr.push(sortedArr[i]);
        }
    }

    return newArr;
}


console.log(sortAndSwap([3, 1, 2, 4, 6, 5]));
console.log(sortAndSwap([9, 7, 5, 3, 1, 2, 4, 6, 8]));
console.log(sortAndSwap([1, 2, 3, 4, 5, 6, 7, 8, 9]));
console.log(sortAndSwap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]));
console.log(sortAndSwap([100, -50, 0, 75, -25, 50, -75, 25]));
console.log(sortAndSwap([5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2]));
