/*
Purge Most Frequent
Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

If multiple values are tied for most frequent, remove all of them.
Do not change any of the other elements or their order.

1. purge_most_frequent([1, 2, 2, 3]) should return [1, 3].
2. purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]) should return ["a", "b", "b", "c", "c", "c"].
3. purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]) should return ["red", "green", "red", "green"].
4. purge_most_frequent([5, 5, 5, 5]) should return [].
 */

function purgeMostFrequent(arr) {

    return arr;
}


console.log(purgeMostFrequent([1, 2, 2, 3]));
console.log(purgeMostFrequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]));
console.log(purgeMostFrequent(["red", "blue", "green", "red", "blue", "green", "blue"]));
console.log(purgeMostFrequent([5, 5, 5, 5]));
