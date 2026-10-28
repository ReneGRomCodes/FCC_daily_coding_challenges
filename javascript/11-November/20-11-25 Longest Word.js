/*
Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.

1. longest_word("The quick red fox") should return "quick".
2. longest_word("Hello coding challenge.") should return "challenge".
3. longest_word("Do Try This At Home.") should return "This".
4. longest_word("This sentence... has commas, ellipses, and an exlamation point!") should return "exlamation".
5. longest_word("A tie? No way!") should return "tie".
6. longest_word("Wouldn't you like to know.") should return "Wouldnt".
 */

function longestWord(sentence) {
    let cleanedSentence = [];
    let longestWord = "";

    // Remove non-alphabetic characters from sentence.
    for (const char of sentence) {
        if (/[a-z]/i.test(char) || char === " ") { cleanedSentence.push(char) }
    }

    cleanedSentence = cleanedSentence.join("").split(" ");

    // Find the longest word.
    for (const word of cleanedSentence) {
        if (word.length > longestWord.length) { longestWord = word }
    }

    return longestWord;
}


console.log(longestWord("The quick red fox"));
console.log(longestWord("Hello coding challenge."));
console.log(longestWord("Do Try This At Home."));
console.log(longestWord("This sentence... has commas, ellipses, and an exlamation point!"));
console.log(longestWord("A tie? No way!"));
console.log(longestWord("Wouldn't you like to know."));
