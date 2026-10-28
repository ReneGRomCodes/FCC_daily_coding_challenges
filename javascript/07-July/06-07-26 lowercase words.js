/*
lowercase words
Given a string, return only the words that are entirely lowercase, in their original order and with a space between each
word.

1. get_lowercase_words("hello GOOD world") should return "hello world".
2. get_lowercase_words("these are all lowercase") should return "these are all lowercase".
3. get_lowercase_words("less is NoT more") should return "less is more".
4. get_lowercase_words("DonT eat pizza every OTHER day") should return "eat pizza every day".
5. get_lowercase_words("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog")
    should return "the quick brown fox jumped over the lazy dog".
 */

function getLowercaseWords(str) {
    const words = str.split(" ");
    const lowerCaseWords = [];

    for (const word of words) {
        if (word === word.toLowerCase()) {
            lowerCaseWords.push(word);
        }
    }

    return lowerCaseWords.join(" ");
}


console.log(getLowercaseWords("hello GOOD world"));
console.log(getLowercaseWords("these are all lowercase"));
console.log(getLowercaseWords("less is NoT more"));
console.log(getLowercaseWords("DonT eat pizza every OTHER day"));
console.log(getLowercaseWords("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog"));
