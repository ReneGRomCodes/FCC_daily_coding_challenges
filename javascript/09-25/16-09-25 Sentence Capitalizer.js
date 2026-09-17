/*
Sentence Capitalizer
Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

All other characters should be preserved.
Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).

1. capitalize("this is a simple sentence.") should return "This is a simple sentence.".
2. capitalize("hello world. how are you?") should return "Hello world. How are you?".
3. capitalize("i did today's coding challenge... it was fun!!")
    should return "I did today's coding challenge... It was fun!!".
4. capitalize("crazy!!!strange???unconventional...sentences.")
    should return "Crazy!!!Strange???Unconventional...Sentences.".
5. capitalize("there's a space before this period . why is there a space before that period ?")
    should return "There's a space before this period . Why is there a space before that period ?".
 */

function capitalize(paragraph) {
    const capParagraph = [];
    const specials = ".?!";
    let specialsFound = false;

    for (let i = 0; i < paragraph.length; i++) {
        const char = paragraph[i];

        if (i === 0) {
            capParagraph.push(char.toUpperCase());
            continue;
        } else if (/[A-Za-z]/.test(char) && specialsFound) {
            capParagraph.push(char.toUpperCase());
            specialsFound = false;
            continue;
        } else if (specials.includes(char)) {
            specialsFound = true;
        }

        capParagraph.push(char);
    }

    return capParagraph.join("");
}


console.log(capitalize("this is a simple sentence."));
console.log(capitalize("hello world. how are you?"));
console.log(capitalize("i did today's coding challenge... it was fun!!"));
console.log(capitalize("crazy!!!strange???unconventional...sentences."));
console.log(capitalize("there's a space before this period . why is there a space before that period ?"));
