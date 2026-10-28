/*
Jbelmud Text
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase.

1. jbelmu("hello world") should return "hello wlord".
2. jbelmu("i love jumbled text") should return "i love jbelmud text".
3. jbelmu("freecodecamp is my favorite place to learn to code")
    should return "faccdeeemorp is my faiortve pacle to laern to cdoe".
4. jbelmu("the quick brown fox jumps over the lazy dog") should return "the qciuk borwn fox jmpus oevr the lazy dog".
 */

const jbelmu = (text) =>
    text
        .split(" ")
        .map((word) => {
            if (word.length <= 3) {
                return word;
            }

            const middle = word
                .slice(1, -1)
                .split("")
                .sort()
                .join("");

            return `${word[0]}${middle}${word.at(-1)}`;
        })
        .join(" ");


console.log(jbelmu("hello world"));
console.log(jbelmu("i love jumbled text"));
console.log(jbelmu("freecodecamp is my favorite place to learn to code"));
console.log(jbelmu("the quick brown fox jumps over the lazy dog"));
