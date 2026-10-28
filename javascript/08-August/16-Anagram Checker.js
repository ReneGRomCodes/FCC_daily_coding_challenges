/*
Anagram Checker
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

Ignore casing and white space.

1. are_anagrams("listen", "silent") should return true.
2. are_anagrams("School master", "The classroom") should return true.
3. are_anagrams("A gentleman", "Elegant man") should return true.
4. are_anagrams("Hello", "World") should return false.
5. are_anagrams("apple", "banana") should return false.
6. are_anagrams("cat", "dog") should return false.
 */

function areAnagrams(str1, str2) {
    const strList1 = str1.replaceAll(" ", "").toLowerCase().split("").sort().join("");
    const strList2 = str2.replaceAll(" ", "").toLowerCase().split("").sort().join("");

    return strList1 === strList2;
}


console.log(areAnagrams("listen", "silent"));
console.log(areAnagrams("School master", "The classroom"));
console.log(areAnagrams("A gentleman", "Elegant man"));
console.log(areAnagrams("Hello", "World"));
console.log(areAnagrams("apple", "banana"));
console.log(areAnagrams("cat", "dog"));
