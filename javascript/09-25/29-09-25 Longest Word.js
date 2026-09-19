/*
Longest Word
Given a sentence, return the longest word in the sentence.

Ignore periods (.) when determining word length.
If multiple words are ties for the longest, return the first one that occurs.

1. get_longest_word("coding is fun") should return "coding".
2. get_longest_word("Coding challenges are fun and educational.") should return "educational".
3. get_longest_word("This sentence has multiple long words.") should return "sentence".
 */

function getLongestWord(sentence) {
    const words = sentence.split(" ").map(x => x.replace(".", ""));
    let longestWord = "";

    for (const word of words) {
        if (word.length > longestWord.length) { longestWord = word }
    }

    return longestWord;
}


console.log(getLongestWord("coding is fun"));
console.log(getLongestWord("Coding challenges are fun and educational."));
console.log(getLongestWord("This sentence has multiple long words."));
