/*
Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element.

1. most_frequent(["a", "b", "a", "c"]) should return "a".
2. most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) should return 2.
3. most_frequent([True, False, "False", "True", False]) should return False.
4. most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]) should return 40.
 */

function mostFrequent(arr) {
    const hist = {};

    for (const item of arr) {
        if (hist[item] === undefined) {
            hist[item] = 1;
        } else {
            hist[item]++;
        }
    }

    return arr.reduce((a, b) => hist[a] >= hist[b] ? a : b);
}


console.log(mostFrequent(["a", "b", "a", "c"]));
console.log(mostFrequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]));
console.log(mostFrequent([true, false, "False", "True", false]));
console.log(mostFrequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]));
