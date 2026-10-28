/*
Array Diff
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.

1. array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) should return ["cherry"].
2. array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) should return ["cherry"].
3. array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])
    should return ["eight", "four", "six", "two"].
4. array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"])
    should return ["five", "one", "seven", "three"].
5. array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]) should return ["freeCodeCamp", "rocks"].
 */

function arrayDiff(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);

    const onlyIn1 = arr1.filter(x => !set2.has(x));
    const onlyIn2 = arr2.filter(x => !set1.has(x));

    return [...new Set([...onlyIn1, ...onlyIn2])].sort();
}


console.log(arrayDiff(["apple", "banana"], ["apple", "banana", "cherry"]));
console.log(arrayDiff(["apple", "banana", "cherry"], ["apple", "banana"]));
console.log(arrayDiff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]));
console.log(arrayDiff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]));
console.log(arrayDiff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]));
