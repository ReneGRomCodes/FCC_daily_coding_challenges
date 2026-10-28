/*
Word Score

Given a word, return its score using a standard letter-value table:
Letter	Value
     A      1
     B      2
   ...    ...
     Z     26

Upper and lowercase letters have the same value.

1. get_word_score("hi") should return 17.
2. get_word_score("hello") should return 52.
3. get_word_score("hippopotamus") should return 169.
4. get_word_score("freeCodeCamp") should return 94.
 */

function getWordScore(word) {
    let value = 0;

    for (let i = 0; i < word.length; i++) {
        value += word.toLowerCase().charCodeAt(i) - 96;
    }

    return value;
}


console.log(getWordScore("hi"));
console.log(getWordScore("hello"));
console.log(getWordScore("hippopotamus"));
console.log(getWordScore("freeCodeCamp"));
