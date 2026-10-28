/*
Pig Latin Converter
Given a string, convert it to Pig Latin using the following rules:

- If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to
  "universeway".
- If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to
  "ellohay".
- Preserve the case of the first letter. For example, "Hello" converts to "Ellohay".

1. pig_latin("universe") should return "universeway".
2. pig_latin("hello") should return "ellohay".
3. pig_latin("hello universe") should return "ellohay universeway".
4. pig_latin("Hello universe") should return "Ellohay universeway".
5. pig_latin("Pig Latin is fun") should return "Igpay Atinlay isway unfay".
6. pig_latin("The quick brown fox jumped over the lazy dog")
    should return "Ethay uickqay ownbray oxfay umpedjay overway ethay azylay ogday".
 */

function pigLatin(str) {
    return str.split(' ').map(word => {
        if (/^[aeiou]/i.test(word)) {
            return word + "way";
        }

        const vowelIdx = word.search(/[aeiou]/i);

        if (vowelIdx === -1) return word;

        const consonants = word.slice(0, vowelIdx);
        const rest = word.slice(vowelIdx);
        const newWord = rest + consonants + "ay";

        if (word[0] === word[0].toUpperCase()) {
            return newWord.charAt(0).toUpperCase() + newWord.slice(1).toLowerCase();
        }

        return newWord.toLowerCase();

    }).join(' ');
}


console.log(pigLatin("universe"));
console.log(pigLatin("hello"));
console.log(pigLatin("hello universe"));
console.log(pigLatin("Hello universe"));
console.log(pigLatin("Pig Latin is fun"));
console.log(pigLatin("The quick brown fox jumped over the lazy dog"));
