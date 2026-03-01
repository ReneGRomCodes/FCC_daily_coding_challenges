/*
Flattened
Given an array, determine if it is flat.

An array is flat if none of its elements are arrays.

1. is_flat([1, 2, 3, 4]) should return True.
2. is_flat([1, [2, 3], 4]) should return False.
3. is_flat([1, 0, False, True, "a", "b"]) should return True.
4. is_flat(["a", [0], "b", True]) should return False.
5. is_flat([1, [2, [3, [4, [5]]]], 6]) should return False.
 */

function isFlat(arr) {
    for (let item of arr) {
        if (typeof item === "object") {
            return false;
        }
    }

    return true;
}


console.log(isFlat([1, 2, 3, 4]));
console.log(isFlat([1, [2, 3], 4]));
console.log(isFlat([1, 0, false, true, "a", "b"]));
console.log(isFlat(["a", [0], "b", true]));
console.log(isFlat([1, [2, [3, [4, [5]]]], 6]));
