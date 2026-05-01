/*
Anagram Groups
Given an array of words, return a 2d array of the words grouped into anagrams.

- Words are anagrams if they contain the same letters in any order.
- Each word belongs to exactly one group.
- Return order doesn't matter.

For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"],
["world"]].

1. group_anagrams(["listen", "silent", "hello", "enlist", "world"]) should return [["listen", "silent", "enlist"], ["hello"], ["world"]].
2. group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) should return [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]].
3. group_anagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"])
    should return [["acre", "care", "race"], ["evil", "live", "veil", "vile"], ["opts", "post", "pots", "spot", "stop", "tops"]].
4. group_anagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"])
    should return [["alerting", "integral", "relating", "triangle"], ["algorithms", "logarithms"], ["auctioned", "cautioned", "education"]].
 */

const groupAnagrams = (words) => {
    const groups = {};

    for (const word of words) {
        const key = [...word].sort().join("");

        if (!groups[key]) {
            groups[key] = [];
        }

        groups[key].push(word);
    }

    return Object.values(groups);
};


console.log(groupAnagrams(["listen", "silent", "hello", "enlist", "world"]));
console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
console.log(groupAnagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]));
console.log(groupAnagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]));
