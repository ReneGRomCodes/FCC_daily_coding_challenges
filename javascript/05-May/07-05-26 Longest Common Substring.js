/*
Longest Common Substring
Given a string, return the longest substring that appears more than once.

- The substrings can overlap.

1. get_longest_substring("abracadabra") should return "abra".
2. get_longest_substring("hello world hello") should return "hello".
3. get_longest_substring("mississippi") should return "issi".
4. get_longest_substring("ha ha ha ha ha ha ha") should return "ha ha ha ha ha ha".
5. get_longest_substring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over")
    should return "the quick brown fox jumped over".
 */

function getLongestSubstring(str) {
    const maxWindowSize = str.length - 1;
    for (let size = maxWindowSize; size > 0; size--) {

        for (let start = 0; start <= str.length - size; start++) {
            const window = str.substring(start, start + size);

            if (str.indexOf(window) !== str.lastIndexOf(window)) {
                return window;
            }
        }
    }
    return "";
}


console.log(getLongestSubstring("abracadabra"));
console.log(getLongestSubstring("hello world hello"));
console.log(getLongestSubstring("mississippi"));
console.log(getLongestSubstring("ha ha ha ha ha ha ha"));
console.log(getLongestSubstring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over"));
