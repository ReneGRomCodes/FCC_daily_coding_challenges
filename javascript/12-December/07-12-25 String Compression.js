/*
String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by
the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".

1. compress_string("yes yes yes please") should return "yes(3) please".
2. compress_string("I have have have apples") should return "I have(3) apples".
3. compress_string("one one three and to the the the the") should return "one(2) three and to the(4)".
4. compress_string("route route route route route route tee tee tee tee tee tee") should return "route(6) tee(6)".
 */

function compressString(sentence) {
    // This solution is far from perfect. Duplicate words are counted throughout the sentence, not only if they are
    // consecutive. This one is does fulfill the challenge requirements and is easy to read though.
    const counted = [];
    const newSentence = [];

    for (const word of sentence.split(" ")) {
        if (!counted.some(([w, count]) => w === word && count === sentence.split(word).length - 1)) {
            counted.push([word, sentence.split(word).length - 1]);
        }
    }

    for (const count of counted) {
        if (count[1] > 1) { newSentence.push(`${count[0]}(${count[1]}) `) }
        else { newSentence.push(`${count[0]} `) }
    }

    return newSentence.join("").trimEnd();
}


function compressStringAlternative(sentence) {
    // More thorough solution to the challenge which takes non-consecutive duplicates into account.
    const words = sentence.split(" ");
    const result = [];
    let current = words[0];
    let count = 1;

    for (const word of words.slice(1)) {
        if (word === current) { count++ }
        else {
            if (count > 1) { result.push(`${current}(${count})`) }
            else { result.push(current) }

        current = word;
        count = 1;
        }
    }

    // Handle the last word/run.
    if (count > 1) { result.push(`${current}(${count})`) }
    else { result.push(current) }

    return result.join(" ");
}


console.log(compressString("yes yes yes please"));
console.log(compressString("I have have have apples"));
console.log(compressString("one one three and to the the the the"));
console.log(compressString("route route route route route route tee tee tee tee tee tee"));
