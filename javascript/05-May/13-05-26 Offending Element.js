/*
Offending Element
Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.

If more than one element could be considered out of place, return the index of the first one.

1. find_offender([1, 6, 2, 3, 4, 5]) should return 1.
2. find_offender([1, 2, 3, 5, 4, 5]) should return 3.
3. find_offender([2, 1]) should return 0.
4. find_offender([2, 4, 1, 6, 8]) should return 2.
5. find_offender([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]) should return 6.
 */

function findOffender(arr) {

    for (let i = 0; i < arr.length; i++) {
        const n = arr[i];
        const prevOk = (i === 0 || arr[i - 1] <= n);
        const nextOk = (i === arr.length - 1 || n <= arr[i + 1])

        if (!prevOk || !nextOk) {
            if (i === 0 || i === arr.length - 1) {
                return i;
            } else if (n > arr[i + 1] && arr[i - 1] > arr[i + 1]) {
                return i + 1;
            } return i;
        }
    }
}


console.log(findOffender([1, 6, 2, 3, 4, 5]));
console.log(findOffender([1, 2, 3, 5, 4, 5]));
console.log(findOffender([2, 1]));
console.log(findOffender([2, 4, 1, 6, 8]));
console.log(findOffender([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]));
