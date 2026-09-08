/*
Vowel Repeater
Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel
you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear
twice in a row. The third vowel should appear three times in a row, and so on.

The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
The original vowel should keeps its case.
Repeated vowels should be lowercase.
All non-vowel characters should keep their original case.

1. repeat_vowels("hello world") should return "helloo wooorld".
2. repeat_vowels("freeCodeCamp") should return "freeeCooodeeeeCaaaaamp".
3. repeat_vowels("AEIOU") should return "AEeIiiOoooUuuuu".
4. repeat_vowels("I like eating ice cream in Iceland") should return "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee
    creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand".
 */

function repeatVowels(str) {
    const vowels = ["a", "e", "i", "o", "u"];
    let vowelRepeatCounter = 0;
    const new_str = [];

    for (const char of str) {
        if (vowels.includes(char.toLowerCase())) {
            new_str.push(char + char.toLowerCase().repeat(vowelRepeatCounter));
            vowelRepeatCounter++;
        } else {
            new_str.push(char);
        }
    }

    return new_str.join("");
}


console.log(repeatVowels("hello world"));
console.log(repeatVowels("freeCodeCamp"));
console.log(repeatVowels("AEIOU"));
console.log(repeatVowels("I like eating ice cream in Iceland"));
