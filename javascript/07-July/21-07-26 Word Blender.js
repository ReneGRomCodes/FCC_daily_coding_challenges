/*
Word Blender
Given two words, return a new word by combining the first half of the first word with the second half of the second word.

- For odd-length words, the first half is the shorter half.

1. blend_words("turtle", "toucan") should return "turcan".
2. blend_words("chipmunk", "flamingo") should return "chipingo".
3. blend_words("falcon", "pelican") should return "falican".
4. blend_words("hyena", "iguana") should return "hyana".
5. blend_words("scorpion", "gorilla") should return "scorilla".
6. blend_words("platypus", "wolverine") should return "platerine".
 */

function blendWords(word1, word2) {
    return word1.slice(0, Math.floor(word1.length / 2)) + word2.slice(Math.floor(word2.length / 2));
}


console.log(blendWords("turtle", "toucan"));
console.log(blendWords("chipmunk", "flamingo"));
console.log(blendWords("falcon", "pelican"));
console.log(blendWords("hyena", "iguana"));
console.log(blendWords("scorpion", "gorilla"));
console.log(blendWords("platypus", "wolverine"));
