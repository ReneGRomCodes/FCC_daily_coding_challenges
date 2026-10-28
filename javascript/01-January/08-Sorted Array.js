/*
Sorted Array?
Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

In ascending order (lowest to highest), return "Ascending".
In descending order (highest to lowest), return "Descending".
Not sorted in ascending or descending order, return "Not sorted".

1. is_sorted([1, 2, 3, 4, 5]) should return "Ascending".
2. is_sorted([10, 8, 6, 4, 2]) should return "Descending".
3. is_sorted([1, 3, 2, 4, 5]) should return "Not sorted".
4. is_sorted([3.14, 2.71, 1.61, 0.57]) should return "Descending".
5. is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]) should return "Ascending".
6. is_sorted([0.4, 0.5, 0.3]) should return "Not sorted".
 */

function isSorted(arr) {
    if ([...arr].sort((a, b) => a - b).every((x, i) => x === arr[i])) {
        return "Ascending";
    } else if ([...arr].sort((a, b) => b - a).every((x, i) => x === arr[i])) {
        return "Descending";
    }

    return "Not sorted";
}


console.log(isSorted([1, 2, 3, 4, 5]));
console.log(isSorted([10, 8, 6, 4, 2]));
console.log(isSorted([1, 3, 2, 4, 5]));
console.log(isSorted([3.14, 2.71, 1.61, 0.57]));
console.log(isSorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]));
console.log(isSorted([0.4, 0.5, 0.3]));
