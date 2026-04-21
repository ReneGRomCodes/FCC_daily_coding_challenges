/*
Odd Words
Given a string of words, return only the words with an odd number of letters.

- Words in the given string will be separated by a single space.
- Return the words separated by a single space.

1. get_odd_words("This is a super good test") should return "a super".
2. get_odd_words("one two three four") should return "one two three".
3. get_odd_words("banana split sundae with rainbow sprinkles on top") should return "split rainbow sprinkles top".
4. get_odd_words("The quick brown fox jumped over the lazy river") should return "The quick brown fox the river".
 */

function getOddWords(str) {
    return str
        .split(" ")
        .filter(word => word.length % 2 !== 0)
        .join(" ");
}


console.log(getOddWords("This is a super good test"));
console.log(getOddWords("one two three four"));
console.log(getOddWords("banana split sundae with rainbow sprinkles on top"));
console.log(getOddWords("The quick brown fox jumped over the lazy river"));
