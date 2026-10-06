/*
Word Counter
Given a sentence string, return the number of words that are in the sentence.

Words are any sequence of non-space characters and are separated by a single space.

1. count_words("Hello world") should return 2.
2. count_words("The quick brown fox jumps over the lazy dog.") should return 9.
3. count_words("I like coding challenges!") should return 4.
4. count_words("Complete the challenge in JavaScript and Python.") should return 7.
5. count_words("The missing semi-colon crashed the entire internet.") should return 7.
 */

function countWords(sentence) { return sentence.split(" ").length }


console.log(countWords("Hello world"));
console.log(countWords("The quick brown fox jumps over the lazy dog."));
console.log(countWords("I like coding challenges!"));
console.log(countWords("Complete the challenge in JavaScript and Python."));
console.log(countWords("The missing semi-colon crashed the entire internet."));
