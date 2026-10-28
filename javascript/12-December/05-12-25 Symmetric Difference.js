/*
Symmetric Difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.

1. difference([1, 2, 3], [3, 4, 5]) should return [1, 2, 4, 5].
2. difference(["a", "b"], ["c", "b"]) should return ["a", "c"].
3. difference([1, "a", 2], [2, "b", "a"]) should return [1, "b"].
4. difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [2, 4, 6, 8].
 */

function difference(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);
    const diffSet = new Set([
        ...[...set1].filter(item => !set2.has(item)),
        ...[...set2].filter(item => !set1.has(item))
    ]);

    const diffList = [];
    for (const item of [...arr1, ...arr2]) {
        if (diffSet.has(item) && !diffList.includes(item)) {
            diffList.push(item);
        }
    }

    return diffList;
}


console.log(difference([1, 2, 3], [3, 4, 5]));
console.log(difference(["a", "b"], ["c", "b"]));
console.log(difference([1, "a", 2], [2, "b", "a"]));
console.log(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]));
