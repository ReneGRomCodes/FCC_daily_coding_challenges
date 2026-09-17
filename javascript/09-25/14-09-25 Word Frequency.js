/*
Word Frequency
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first.

1. get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding")
    should return ["coding", "python", "in"].
2. get_words("I like coding. I like testing. I love debugging!") should return ["i", "like", "coding"].
3. get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!")
    should return ["debug", "test", "deploy"].
 */

function getWords(paragraph) {
    const words = paragraph.split(" ");
    const wordsHist = {};

    for (let word of words) {
        word = word.replace(/^[.,!]+|[.,!]+$/g, "").toLowerCase();

        if (word in wordsHist) {
            wordsHist[word]++;
        } else {
            wordsHist[word] = 1;
        }
    }

    const mostFrequentWords = Object.keys(wordsHist)
        .sort((a, b) => wordsHist[b] - wordsHist[a])
        .slice(0, 3);

    return mostFrequentWords;
}


console.log(getWords("Coding in Python is fun because coding Python allows for coding in Python easily while coding"));
console.log(getWords("I like coding. I like testing. I love debugging!"));
console.log(getWords("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"));
